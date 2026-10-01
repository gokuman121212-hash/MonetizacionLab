# ==============================================================================
# Módulo Core: PISShopifyCompiler (Generador Multi-Página Estilo Shopify)
# ==============================================================================
import os
import json
from datetime import datetime

class PISShopifyCompiler:
    def __init__(self, config_path="data/config.json", data_path="data/keywords.json", output_dir="output"):
        self.config_path = config_path
        self.data_path = data_path
        self.output_dir = output_dir
        
    def cargar_recursos(self):
        try:
            with open(self.config_path, "r", encoding="utf-8-sig") as f:
                self.config = json.load(f)
            with open(self.data_path, "r", encoding="utf-8-sig") as f:
                self.items = json.load(f)
            with open("templates/shopify_theme/index_template.html", "r", encoding="utf-8-sig") as f:
                self.t_index = f.read()
            with open("templates/shopify_theme/specs_template.html", "r", encoding="utf-8-sig") as f:
                self.t_specs = f.read()
            with open("templates/shopify_theme/support_template.html", "r", encoding="utf-8-sig") as f:
                self.t_support = f.read()
            os.makedirs(self.output_dir, exist_ok=True)
            return True
        except Exception as e:
            print(f"[Error de Carga] No se pudieron inicializar los recursos: {e}")
            return False

    def compilar(self):
        if not self.cargar_recursos():
            return
            
        print(f"=== [PSEO Enterprise v9.0] Compilando Ecosistema Multi-Página Estilo Shopify ===")
        urls_sitemap = []
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        for idx, item in enumerate(self.items, 1):
            # Creamos una subcarpeta por cada servicio para que tenga su propio ecosistema limpio
            slug_dir = os.path.join(self.output_dir, item['slug'])
            os.makedirs(slug_dir, exist_ok=True)
            
            # Datos comunes a reemplazar
            replacements = [
                ("{{IDIOMA}}", self.config["idioma"]),
                ("{{SITIO_NOMBRE}}", self.config["sitio_nombre"]),
                ("{{WHATSAPP}}", self.config["contacto_whatsapp"].replace("+", "")),
                ("{{CATEGORIA}}", item["categoria"]),
                ("{{TITULO}}", item["titulo"]),
                ("{{PRECIO}}", item["precio"]),
                ("{{DESCRIPCION}}", item["desc"])
            ]
            
            # 1. Generar index.html principal del servicio
            html_idx = self.t_index
            for k, v in replacements:
                html_idx = html_idx.replace(k, v)
            with open(os.path.join(slug_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_idx)
                
            # 2. Generar especificaciones.html secundaria real
            html_specs = self.t_specs
            for k, v in replacements:
                html_specs = html_specs.replace(k, v)
            with open(os.path.join(slug_dir, "especificaciones.html"), "w", encoding="utf-8") as f:
                f.write(html_specs)
                
            # 3. Generar soporte.html secundaria real
            html_sup = self.t_support
            for k, v in replacements:
                html_sup = html_sup.replace(k, v)
            with open(os.path.join(slug_dir, "soporte.html"), "w", encoding="utf-8") as f:
                f.write(html_sup)
                
            urls_sitemap.append(f"{self.config['dominio_base']}/{item['slug']}/index.html")
            print(f"[{idx}/35] Ecosistema Shopify compilado para -> {item['slug']}")

        # Generar Sitemap XML
        sitemap_path = os.path.join(self.output_dir, "sitemap.xml")
        sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls_sitemap:
            sitemap_xml += f'  <url><loc>{url}</loc><lastmod>{fecha_actual}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>\n'
        sitemap_xml += '</urlset>'
        
        with open(sitemap_path, "w", encoding="utf-8") as sm:
            sm.write(sitemap_xml)
            
        print(f"\n[Éxito Total v9.0] 35 ecosistemas web independientes generados con diseño Shopify.")
