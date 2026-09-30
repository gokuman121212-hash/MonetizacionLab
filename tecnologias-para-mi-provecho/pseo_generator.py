# [Tecnologías para mi provecho] - Automatización y pSEO personal
import os

def generar_recursos_propios():
    print("=== [MonetizacionLab] Automatización Personal Activa ===" )
    print("Generando recursos y páginas optimizadas para uso propio...")
    
    os.makedirs("output_local", exist_ok=True)
    with open("output_local/index.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html><html><head><title>Mi Herramienta pSEO</title></head><body><h1>Panel Propio</h1><p>Generado automáticamente.</p></body></html>")
        
    print("[Éxito] Estructura propia generada en 'output_local'.")

if __name__ == "__main__":
    generar_recursos_propios()
