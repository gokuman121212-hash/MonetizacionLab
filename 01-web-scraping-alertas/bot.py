import requests
from bs4 import BeautifulSoup

def buscar_oportunidades():
    print("=== [MonetizacionLab] Bot de Web Scraping Activo ===")
    print("Buscando ofertas y oportunidades locales...")
    url = "https://httpbin.org/html"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titulo = soup.find('h1')
            print(f"[Éxito] Conexión establecida. Elemento encontrado: {titulo.text if titulo else 'Sin título'}")
        else:
            print("[Error] No se pudo acceder a la página.")
    except Exception as e:
        print(f"[Error de conexión] {e}")

if __name__ == "__main__":
    buscar_oportunidades()
