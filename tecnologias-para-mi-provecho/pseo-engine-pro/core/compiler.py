# ==============================================================================
# Módulo Core: PSEOTierCompiler (Generador Multi-Tier por Niveles de Complejidad)
# ==============================================================================
import os
import json
from datetime import datetime

class PSEOTierCompiler:
    def __init__(self, config_path="data/config.json", data_path="data/keywords.json", template_path="templates/master_template.html", output_dir="output"):
        self.config_path = config_path
        self.data_path = data_path
        self.template_path = template_path
        self.output_dir = output_dir
        
    def cargar_recursos(self):
        try:
            with open(self.config_path, "r", encoding="utf-8-sig") as f:
                self.config = json.load(f)
            with open(self.data_path, "r", encoding="utf-8-sig") as f:
                self.items = json.load(f)
            with open(self.template_path, "r", encoding="utf-8-sig") as f:
                self.template = f.read()
            os.makedirs(self.output_dir, exist_ok=True)
            return True
        except Exception as e:
            print(f"[Error de Carga] No se pudieron inicializar los recursos: {e}")
            return False

    def obtener_configuracion_tier(self, tier):
        # Define los apartados según el nivel de complejidad solicitado
        if tier == 1:
            return 4, "Nivel 1 (Simple - 4 Apartados)", ["index.html", "catalogo.html", "checkout.html", "contacto.html"]
        elif tier == 2:
            return 10, "Nivel 2 (Medio - 10 Apartados)", ["index.html", "catalogo.html", "productos.html", "detalles.html", "carrito.html", "checkout.html", "blog.html", "nosotros.html", "soporte.html", "contacto.html"]
        elif tier == 3:
            return 20, "Nivel 3 (Avanzado - 20 Apartados)", [f"seccion-{i}.html" for i in range(1, 21)]
        elif tier == 4:
            return 40, "Nivel 4 (Alto Calibre / Enterprise - 40 Apartados)", [f"enterprise-modulo-{i}.html" for i in range(1, 41)]
        else:
            return 4, "Nivel 1 (Simple)", ["index.html", "catalogo.html", "checkout.html", "contacto.html"]

    def compilar(self):
        if not self.cargar_recursos():
            return
            
        tier_nivel = self.config.get("tier_complejidad", 1)
        cantidad_apartados, tier_nombre, lista_paginas = self.obtener_configuracion_tier(tier_nivel)
        
        print(f"=== [PSEO Enterprise v6.0] Compilando Tier {tier_nivel}: {tier_nombre} ({cantidad_apartados} apartados) ===")
        
        urls_sitemap = []
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        # Construir barra de navegación dinámica con las primeras páginas del Tier
        nav_html = ""
        paginas_nav = lista_paginas[:6] # Mostramos hasta 6 en el menú visual para mantener elegancia
        for pag in paginas_nav:
            nombre_amigable = pag.replace(".html", "").replace("-", " ").title()
            nav_html += f'<a href="{pag}">{nombre_amigable}</a>\n'

        # Generar masivamente cada página del Tier interconectada
        for idx, filename in enumerate(lista_paginas, 1):
            file_path = os.path.join(self.output_dir, filename)
            
            # Seleccionar un item de datos de forma rotativa si hay más páginas que datos
            item_data = self.items[(idx - 1) % len(self.items)]
            
            titulo_pag = f"{item_data['nombre']} - Módulo {idx}"
            desc_pag = item_data['descripcion']
            precio_str = f'<div class="price-tag">Inversión: S/ {item_data["precio"]}</div>' if "precio" in item_data else ""
            
            html = self.template
            html = html.replace("{{IDIOMA}}", self.config["idioma"])
            html = html.replace("{{SITIO_NOMBRE}}", self.config["sitio_nombre"])
            html = html.replace("{{COLOR_PRIMARIO}}", self.config["color_primario"])
            html = html.replace("{{COLOR_SECUNDARIO}}", self.config["color_secundario"])
            html = html.replace("{{WHATSAPP}}", self.config["contacto_whatsapp"].replace("+", ""))
            html = html.replace("{{TIER_NOMBRE}}", tier_nombre)
            html = html.replace("{{MODULO_ID}}", f"{idx}/{cantidad_apartados}")
            html = html.replace("{{NAV_LINKS_HTML}}", nav_html)
            html = html.replace("{{TITULO_PAGINA}}", titulo_pag)
            html = html.replace("{{DESCRIPCION_PAGINA}}", desc_pag)
            html = html.replace("{{PRECIO_HTML}}", precio_str)
            
            with open(file_path, "w", encoding="utf-8") as out:
                out.write(html)
                
            urls_sitemap.append(f"{self.config['dominio_base']}/{filename}")
            print(f"[{idx}/{cantidad_apartados}] Módulo compilado con UI fluida -> {filename}")

        # Generación del Sitemap XML optimizado
        sitemap_path = os.path.join(self.output_dir, "sitemap.xml")
        sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls_sitemap:
            sitemap_xml += f'  <url><loc>{url}</loc><lastmod>{fecha_actual}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>\n'
        sitemap_xml += '</urlset>'
        
        with open(sitemap_path, "w", encoding="utf-8") as sm:
            sm.write(sitemap_xml)
            
        print(f"\n[Éxito v6.0] Sistema compilado exitosamente. {cantidad_apartados} apartados generados con diseño de alto calibre.")
