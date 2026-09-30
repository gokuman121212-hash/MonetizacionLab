import json

def generar_catalogo_whatsapp():
    print("=== [MonetizacionLab] Automatizador de Textos para Negocios ===")
    productos = [
        {"nombre": "Pack Emprendedor Digital", "precio": 15.00, "descripcion": "Plantillas y herramientas."},
        {"nombre": "Mantenimiento Preventivo PC", "precio": 30.00, "descripcion": "Optimización de sistema."}
    ]
    plantilla_mensaje = "Hola! 👋 Te presentamos nuestra oferta exclusiva:\n\n"
    for p in productos:
        plantilla_mensaje += f"🔹 *{p['nombre']}*\n   Precio: S/. {p['precio']:.2f}\n   _{p['descripcion']}_\n\n"
    plantilla_mensaje += "Escríbenos para separar el tuyo. ¡Stock limitado!"
    
    print("\n--- Mensaje formateado listo para enviar por WhatsApp ---")
    print(plantilla_mensaje)
    
    with open("catalogo_generado.txt", "w", encoding="utf-8") as f:
        f.write(plantilla_mensaje)
    print("\n[Éxito] El mensaje automatizado se ha guardado en 'catalogo_generado.txt'.")

if __name__ == "__main__":
    generar_catalogo_whatsapp()
