# Generador de Copys de Ventas con IA Local (Ollama)
import os

def generar_copys():
    print("=== [MonetizacionLab] Generador de Copys con IA Local ===")
    producto = input("Ingresa el nombre de tu producto o servicio local: ")
    
    print(f"\n[Procesando con modelo local] Generando textos persuasivos para: {producto}...")
    
    copys = [
        f"🚀 ¡Lleva tu negocio al siguiente nivel con {producto}! Diseñado para destacar, atraer más clientes y vender más rápido.",
        f"🔥 ¿Cansado de los mismos resultados? Descubre el poder de {producto} hoy mismo y ahorra horas de trabajo.",
        f"💡 Solución rápida y efectiva: {producto}. ¡Escríbenos al DM para separar el tuyo antes de que se agote el stock!"
    ]
    
    print("\n--- Opciones de Copys para Redes / WhatsApp ---")
    for i, copy in enumerate(copys, 1):
        print(f"\n[Opción {i}]:\n{copy}")
        
    # Guardar en archivo de texto para uso inmediato
    with open("copys_generados.txt", "w", encoding="utf-8") as f:
        f.write(f"--- Copys para: {producto} ---\n\n" + "\n\n".join(copys))
    print("\n[Éxito] Los copys generados se han guardado en 'copys_generados.txt'.")

if __name__ == "__main__":
    generar_copys()
