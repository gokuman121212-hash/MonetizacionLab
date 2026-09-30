# Mapa de Arquitectura E-commerce: PSEO Engine Pro v5.0
> **Descripción:** Sistema avanzado de generación masiva de catálogos y sitios web comerciales multi-página. Diseñado para gestionar inventarios de productos (ej. 50+ artículos), generando automáticamente una página de índice general (*escaparate*) y páginas de producto individuales con marcado Schema.org de comercio electrónico.

## 📂 Estructura de Directorios del Sistema
\\\	ext
pseo-engine-pro/
│
├── core/
│   └── compiler.py         # Módulo central con la clase PSEOCatalogCompiler (Catálogo + Productos)
├── data/
│   ├── config.json         # Configuración global de la tienda (marca, moneda, WhatsApp)
│   └── keywords.json       # Base de datos de inventario y productos comerciales
├── templates/
│   ├── catalog_index.html  # Plantilla maestra de la página principal (escaparate con grilla de productos)
│   └── product.html        # Plantilla maestra de detalle para cada producto con Schema.org Product
├── output/                 # Directorio de salida compilado (index.html + páginas de productos + sitemap.xml)
├── engine.py               # Script de entrada para la ejecución del motor E-commerce
└── MAPA_ARQUITECTURA.md    # Documentación técnica actualizada (Regla de Oro aplicada)
\\\

## 🚀 Capacidades del Sistema v5.0 (E-commerce Multi-página)
1. **Arquitectura de Catálogo y Subpáginas:** Capacidad de leer cientos de productos y estructurar un sitio web completo con navegación cruzada (desde el índice principal hacia cada producto y viceversa).
2. **Schema.org Product (JSON-LD):** Inyección automática de metadatos de comercio electrónico en cada producto individual para optimizar la indexación en motores de búsqueda.
3. **Escalabilidad Masiva:** Permite escalar fácilmente de 5 a 50 o 500 productos simplemente ampliando el archivo JSON de datos.
4. **Sitemap Dinámico Completo:** Generación de un sitemap que indexa tanto la página principal como todas las fichas de productos individuales.
