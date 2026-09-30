# ==========================================
# PSEO Engine Pro - Script de Compilación Masiva
# ==========================================
import os
import json

def compilar_sitios_pseo():
    print("=== [PSEO Engine Pro] Iniciando compilación masiva ===")
    
    # 1. Cargar datos
    data_path = "data/keywords.json"
    template_path = "templates/base.html"
    output_dir = "output"
    
    if not os.path.exists(data_path) or not os.path.exists(template_path):
        print("[Error] No se encontraron los archivos de configuración o la plantilla.")
        return
        
    with open(data_path, "r", encoding="utf-8") as f:
        items = json.load(f)
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. Procesar cada combinación de forma programática
    generados = 0
    for idx, item in enumerate(items, 1):
        kw = item["keyword"]
        loc = item["ubicacion"]
        beneficio = item["beneficio"]
        
        # Generar slugs limpios para los nombres de archivo
        filename = f"{kw.replace(' ', '-')}-{loc.lower().replace(' ', '-')}.html"
        file_path = os.path.join(output_dir, filename)
        
        # Reemplazar variables dinámicas en la plantilla
        page_html = template_content
        page_html = page_html.replace("{{TITLE}}", f"{kw.title()} en {loc} | Servicio Profesional")
        page_html = page_html.replace("{{HEADING}}", f"{kw.title()} Profesional en {loc}")
        page_html = page_html.replace("{{KEYWORD}}", kw)
        page_html = page_html.replace("{{UBICACION}}", loc)
        page_html = page_html.replace("{{BENEFICIO}}", beneficio)
        
        # Escribir archivo estático optimizado
        with open(file_path, "w", encoding="utf-8") as out_file:
            out_file.write(page_html)
            
        print(f"[{idx}] Compilado con éxito: {filename}")
        generados += 1
        
    print(f"\n[Éxito Total] Se han generado {generados} páginas estáticas optimizadas en la carpeta '{output_dir}/'.")

if __name__ == "__main__":
    compilar_sitios_pseo()
