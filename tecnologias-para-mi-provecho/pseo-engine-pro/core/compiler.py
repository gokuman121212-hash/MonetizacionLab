# ==============================================================================
# Módulo Core: PSEOEnterpriseCompiler (Orientado a Clases)
# ==============================================================================
import os
import json
from datetime import datetime

class PSEOEnterpriseCompiler:
    def __init__(self, config_path="data/config.json", data_path="data/keywords.json", template_path="templates/base.html", output_dir="output"):
        self.config_path = config_path
        self.data_path = data_path
        self.template_path = template_path
        self.output_dir = output_dir
        
    def cargar_recursos(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            with open(self.data_path, "r", encoding="utf-8") as f:
                self.items = json.load(f)
            with open(self.template_path, "r", encoding="utf-8") as f:
                self.template = f.read()
            os.makedirs(self.output_dir, exist_ok=True)
            return True
        except Exception as e:
            print(f"[Error de Carga] No se pudieron inicializar los recursos: {e}")
            return False

    def compilar(self):
        if not self.cargar_recursos():
            return
            
        print(f"=== [PSEO Enterprise v4.0] Compilando con Arquitectura de Clases ===")
        urls_sitemap = []
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        for idx, item in enumerate(self.items, 1):
            kw = item["keyword"]
            loc = item["ubicacion"]
            beneficio = item["beneficio"]
            intencion = item["intencion"]
            precio = item["precio_estimado"]
            
            filename = f"{kw.replace(' ', '-')}-{loc.lower().replace(' ', '-')}.html"
            file_path = os.path.join(self.output_dir, filename)
            
            titulo_seo = f"{kw.title()} en {loc} | {self.config['sitio_nombre']}"
            desc_seo = f"Servicio profesional de {kw} en {loc}. {beneficio}. Contáctanos para atención inmediata."
            
            # Renderizado de variables corporativas
            html = self.template
            html = html.replace("{{IDIOMA}}", self.config["idioma"])
            html = html.replace("{{TITLE}}", titulo_seo)
            html = html.replace("{{DESCRIPTION}}", desc_seo)
            html = html.replace("{{COLOR_PRIMARIO}}", self.config["color_primario"])
            html = html.replace("{{UBICACION}}", loc)
            html = html.replace("{{INTENCION}}", intencion)
            html = html.replace("{{KEYWORD}}", kw)
            html = html.replace("{{BENEFICIO}}", beneficio)
            html = html.replace("{{PRECIO}}", precio)
            html = html.replace("{{WHATSAPP}}", self.config["contacto_whatsapp"].replace("+", ""))
            html = html.replace("{{SITIO_NOMBRE}}", self.config["sitio_nombre"])
            
            with open(file_path, "w", encoding="utf-8") as out:
                out.write(html)
                
            urls_sitemap.append(f"{self.config['dominio_base']}/{filename}")
            print(f"[{idx}] Compilación Enterprise OK -> {filename}")
            
        # Generación de Sitemap XML Estándar
        sitemap_path = os.path.join(self.output_dir, "sitemap.xml")
        sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls_sitemap:
            sitemap_xml += f'  <url><loc>{url}</loc><lastmod>{fecha_actual}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>\n'
        sitemap_xml += '</urlset>'
        
        with open(sitemap_path, "w", encoding="utf-8") as sm:
            sm.write(sitemap_xml)
            
        print(f"\n[Éxito Enterprise] {len(self.items)} páginas compiladas y sitemap.xml generado correctamente.")
