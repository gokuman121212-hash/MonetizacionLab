# ==============================================================================
# PSEO Engine Pro - Motor de Compilación Estática y Generación de Sitemap SEO
# ==============================================================================
import os
import json
from datetime import datetime

def compilar_sistema_pseo():
    print("=== [PSEO Engine Pro v3.0] Iniciando compilación de nivel producción ===")
    
    # Rutas
    config_path = "data/config.json"
    data_path = "data/keywords.json"
    template_path = "templates/base.html"
    output_dir = "output"
    
    # Validaciones
    if not os.path.exists(config_path) or not os.path.exists(data_path) or not os.path.exists(template_path):
        print("[Error Crítico] Faltan archivos esenciales de configuración, datos o plantillas.")
        return
        
    # Cargar configuraciones
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    with open(data_path, "r", encoding="utf-8") as f:
        items = json.load(f)
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    os.makedirs(output_dir, exist_ok=True)
    
    urls_sitemap = []
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    # Compilación de páginas
    generadas = 0
    for idx, item in enumerate(items, 1):
        kw = item["keyword"]
        loc = item["ubicacion"]
        beneficio = item["beneficio"]
        intencion = item["intencion"]
        
        filename = f"{kw.replace(' ', '-')}-{loc.lower().replace(' ', '-')}.html"
        file_path = os.path.join(output_dir, filename)
        
        titulo_seo = f"{kw.title()} en {loc} | {config['sitio_nombre']}"
        desc_seo = f"Servicio profesional de {kw} en {loc}. {beneficio}. Atención garantizada y soporte técnico especializado."
        
        # Renderizado de variables
        page_html = template_content
        page_html = page_html.replace("{{IDIOMA}}", config["idioma"])
        page_html = page_html.replace("{{TITLE}}", titulo_seo)
        page_html = page_html.replace("{{DESCRIPTION}}", desc_seo)
        page_html = page_html.replace("{{COLOR_PRIMARIO}}", config["color_primario"])
        page_html = page_html.replace("{{UBICACION}}", loc)
        page_html = page_html.replace("{{INTENCION}}", intencion)
        page_html = page_html.replace("{{KEYWORD}}", kw)
        page_html = page_html.replace("{{BENEFICIO}}", beneficio)
        page_html = page_html.replace("{{WHATSAPP}}", config["contacto_whatsapp"].replace("+", ""))
        page_html = page_html.replace("{{SITIO_NOMBRE}}", config["sitio_nombre"])
        
        with open(file_path, "w", encoding="utf-8") as out_file:
            out_file.write(page_html)
            
        # Registrar URL para el sitemap XML
        url_completa = f"{config['dominio_base']}/{filename}"
        urls_sitemap.append(url_completa)
        
        print(f"[{idx}] Compilado [OK]: {filename}")
        generadas += 1
        
    # Generar Sitemap.xml automático para indexación en motores de búsqueda
    sitemap_path = os.path.join(output_dir, "sitemap.xml")
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls_sitemap:
        sitemap_xml += '  <url>\n'
        sitemap_xml += f'    <loc>{url}</loc>\n'
        sitemap_xml += f'    <lastmod>{fecha_actual}</lastmod>\n'
        sitemap_xml += '    <changefreq>weekly</changefreq>\n'
        sitemap_xml += '    <priority>0.8</priority>\n'
        sitemap_xml += '  </url>\n'
        
    sitemap_xml += '</urlset>'
    
    with open(sitemap_path, "w", encoding="utf-8") as sm_file:
        sm_file.write(sitemap_xml)
        
    print(f"\n[Éxito Senior] Se compilaron {generadas} páginas estáticas y se generó el 'sitemap.xml' listo para SEO técnico.")

if __name__ == "__main__":
    compilar_sistema_pseo()
