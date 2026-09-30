# Mapa de Arquitectura: PSEO Engine Pro
> **Descripción:** Motor de Generación de Contenido Programático (pSEO) automatizado para la creación masiva de páginas web de nicho optimizadas para motores de búsqueda.

## 📂 Estructura de Directorios
\\\	ext
pseo-engine-pro/
│
├── data/
│   └── keywords.json       # Base de datos de palabras clave y variables locales
├── templates/
│   └── base.html           # Plantilla maestra con diseño profesional y responsivo
├── output/                 # Páginas HTML finales generadas automáticamente
├── engine.py               # Script principal de procesamiento y compilación pSEO
└── MAPA_ARQUITECTURA.md    # Este mapa de documentación técnica
\\\

## ⚙️ Flujo de Operación (Workflow)
1. **Entrada de Datos:** \engine.py\ lee las variables y ubicaciones desde \data/keywords.json\.
2. **Procesamiento Masivo:** El motor cruza las palabras clave con la plantilla maestra \	emplates/base.html\.
3. **Compilación Estática:** Se generan archivos HTML independientes optimizados para SEO técnico en la carpeta \output/\.
4. **Despliegue:** Listos para subir de forma gratuita a Vercel, Netlify o GitHub Pages con costo cero.
