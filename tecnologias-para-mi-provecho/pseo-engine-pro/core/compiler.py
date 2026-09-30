# ==============================================================================
# Módulo Core: PSEOIndustryCompiler (Generador Multi-Industria 40 Rubros)
# ==============================================================================
import os
import json
from datetime import datetime

class PSEOIndustryCompiler:
    def __init__(self, config_path="data/config.json", data_path="data/keywords.json", template_path="templates/industry_template.html", output_dir="output"):
        self.config_path = config_path
        self.data_path = data_path
        self.template_path = template_path
        self.output_dir = output_dir
        
    def cargar_recursos(self):
        try:
            with open(self.config_path, "r", encoding="utf-8-sig") as f:
                self.config = json.load(f)
            with open(self.data_path, "r", encoding="utf-8-sig") as f:
                self.rubros_db = json.load(f)
            with open(self.template_path, "r", encoding="utf-8-sig") as f:
                self.template = f.read()
            os.makedirs(self.output_dir, exist_ok=True)
            return True
        except Exception as e:
            print(f"[Error de Carga] No se pudieron inicializar los recursos: {e}")
            return False

    def obtener_schema_por_categoria(self, categoria):
        if categoria == "ecommerce":
            return "Product"
        elif categoria == "servicios_locales":
            return "LocalBusiness"
        elif categoria == "salud_bienestar":
            return "MedicalBusiness"
        elif categoria == "corporativo_inmobiliario":
            return "RealEstateAgent"
        else:
            return "Organization"

    def compilar(self):
        if not self.cargar_recursos():
            return
            
        print("=== [PSEO Enterprise v7.0] Compilando Sistema Multi-Industria (40 Rubros) ===")
        urls_sitemap = []
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        total_compilado = 0
        
        # Recorrer todas las categorías y sus rubros
        for categoria, lista_rubros in self.rubros_db.items():
            schema_type = self.obtener_schema_por_categoria(categoria)
            cat_nombre = categoria.replace("_", " ").title()
            
            for item in lista_rubros:
                filename = f"{item['slug']}.html"
                file_path = os.path.join(self.output_dir, filename)
                
                html = self.template
                html = html.replace("{{IDIOMA}}", self.config["idioma"])
                html = html.replace("{{SITIO_NOMBRE}}", self.config["sitio_nombre"])
                html = html.replace("{{COLOR_PRIMARIO}}", self.config["color_primario"])
                html = html.replace("{{COLOR_SECUNDARIO}}", self.config["color_secundario"])
                html = html.replace("{{WHATSAPP}}", self.config["contacto_whatsapp"].replace("+", ""))
                html = html.replace("{{CATEGORIA_NOMBRE}}", cat_nombre)
                html = html.replace("{{RUBRO_NOMBRE}}", item["rubro"])
                html = html.replace("{{BENEFICIO}}", item["beneficio"])
                html = html.replace("{{SCHEMA_TYPE}}", schema_type)
                html = html.replace("{{TITULO_SECCION}}", f"{item['rubro']} Profesional")
                html = html.replace("{{DESCRIPCION_SECCION}}", f"Solución optimizada para {item['rubro']}. {item['beneficio']}")
                
                with open(file_path, "w", encoding="utf-8") as out:
                    out.write(html)
                    
                urls_sitemap.append(f"{self.config['dominio_base']}/{filename}")
                total_compilado += 1
                print(f"[{total_compilado}] Rubro compilado [{cat_nombre}] -> {filename}")

        # Generar Sitemap XML global optimizado
        sitemap_path = os.path.join(self.output_dir, "sitemap.xml")
        sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls_sitemap:
            sitemap_xml += f'  <url><loc>{url}</loc><lastmod>{fecha_actual}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>\n'
        sitemap_xml += '</urlset>'
        
        with open(sitemap_path, "w", encoding="utf-8") as sm:
            sm.write(sitemap_xml)
            
        print(f"\n[Éxito Total v7.0] {total_compilado} páginas de los 40 rubros generadas e indexadas correctamente.")
