# ==============================================================================
# Módulo Core: PSEOCatalogCompiler (Arquitectura E-commerce Multi-página)
# ==============================================================================
import os
import json
from datetime import datetime

class PSEOCatalogCompiler:
    def __init__(self, config_path="data/config.json", data_path="data/keywords.json", template_product="templates/product.html", template_catalog="templates/catalog_index.html", output_dir="output"):
        self.config_path = config_path
        self.data_path = data_path
        self.template_product = template_product
        self.template_catalog = template_catalog
        self.output_dir = output_dir
        
    def cargar_recursos(self):
        try:
            with open(self.config_path, "r", encoding="utf-8-sig") as f:
                self.config = json.load(f)
            with open(self.data_path, "r", encoding="utf-8-sig") as f:
                self.productos = json.load(f)
            with open(self.template_product, "r", encoding="utf-8-sig") as f:
                self.t_product = f.read()
            with open(self.template_catalog, "r", encoding="utf-8-sig") as f:
                self.t_catalog = f.read()
            os.makedirs(self.output_dir, exist_ok=True)
            return True
        except Exception as e:
            print(f"[Error de Carga] No se pudieron inicializar los recursos: {e}")
            return False

    def compilar(self):
        if not self.cargar_recursos():
            return
            
        print(f"=== [PSEO E-commerce v5.0] Compilando Catálogo y Páginas de Producto ===")
        urls_sitemap = []
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        cards_html = ""
        
        # 1. Compilar páginas individuales de cada producto
        for idx, prod in enumerate(self.productos, 1):
            filename = f"{prod['slug']}.html"
            file_path = os.path.join(self.output_dir, filename)
            
            html = self.t_product
            html = html.replace("{{IDIOMA}}", self.config["idioma"])
            html = html.replace("{{SITIO_NOMBRE}}", self.config["sitio_nombre"])
            html = html.replace("{{COLOR_PRIMARIO}}", self.config["color_primario"])
            html = html.replace("{{MONEDA}}", self.config["moneda"])
            html = html.replace("{{WHATSAPP}}", self.config["contacto_whatsapp"].replace("+", ""))
            
            html = html.replace("{{NOMBRE_PRODUCTO}}", prod["nombre"])
            html = html.replace("{{CATEGORIA}}", prod["categoria"])
            html = html.replace("{{PRECIO}}", prod["precio"])
            html = html.replace("{{DESCRIPCION}}", prod["descripcion"])
            
            with open(file_path, "w", encoding="utf-8") as out:
                out.write(html)
                
            urls_sitemap.append(f"{self.config['dominio_base']}/{filename}")
            print(f"[{idx}] Producto compilado -> {filename}")
            
            # Construir la tarjeta para el índice general
            cards_html += f'''
            <div class="product-card">
                <span class="badge">{prod["categoria"]}</span>
                <h3>{prod["nombre"]}</h3>
                <div class="price">S/ {prod["precio"]}</div>
                <p class="desc">{prod["descripcion"]}</p>
                <a href="{filename}" class="btn-detail">Ver Detalle y Comprar</a>
            </div>
            '''

        # 2. Compilar la página principal del Catálogo (index.html)
        index_path = os.path.join(self.output_dir, "index.html")
        catalog_page = self.t_catalog
        catalog_page = catalog_page.replace("{{IDIOMA}}", self.config["idioma"])
        catalog_page = catalog_page.replace("{{SITIO_NOMBRE}}", self.config["sitio_nombre"])
        catalog_page = catalog_page.replace("{{COLOR_PRIMARIO}}", self.config["color_primario"])
        catalog_page = catalog_page.replace("{{PRODUCT_CARDS_HTML}}", cards_html)
        
        with open(index_path, "w", encoding="utf-8") as out_idx:
            out_idx.write(catalog_page)
            
        urls_sitemap.insert(0, f"{self.config['dominio_base']}/index.html")
        print(f"[Catálogo OK] index.html generado con éxito.")

        # 3. Generar Sitemap XML optimizado con todo el árbol web
        sitemap_path = os.path.join(self.output_dir, "sitemap.xml")
        sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls_sitemap:
            sitemap_xml += f'  <url><loc>{url}</loc><lastmod>{fecha_actual}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\n'
        sitemap_xml += '</urlset>'
        
        with open(sitemap_path, "w", encoding="utf-8") as sm:
            sm.write(sitemap_xml)
            
        print(f"\n[Éxito Total] Catálogo y {len(self.productos)} productos compilados con interconexión SEO.")
