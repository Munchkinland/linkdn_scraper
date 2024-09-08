# LinkedIn Scraper and Sentiment Analysis

## Objetivo del Proyecto

Este proyecto tiene como objetivo realizar un scraping de publicaciones de LinkedIn para una página de empresa, analizar los sentimientos de estas publicaciones y visualizar los resultados de manera interactiva. Utiliza herramientas de scraping web, análisis de sentimientos con modelos de Hugging Face y visualización de datos con Plotly.

## Estructura del Proyecto

- **`.gitignore`**: Archivos y directorios que deben ser ignorados por Git.
- **`.env`**: Archivo para almacenar variables de entorno, como credenciales.
- **`config/`**: Configuración adicional del proyecto.
- **`data/`**: Carpeta que contiene archivos de datos generados por el proyecto.
- **`driver/`**: Contiene el archivo `chromedriver.exe` necesario para Selenium.
- **`scraper.py`**: Script que realiza el scraping de LinkedIn.
- **`sentiment_analysis.py`**: Script que realiza el análisis de sentimientos utilizando modelos de Hugging Face.
- **`plotter.py`**: Script que genera gráficos interactivos con Plotly.
- **`data_loader.py`**: Script para cargar y procesar datos desde archivos Excel.
- **`main.py`**: Script principal que coordina el flujo del proyecto.
- **`estructura_del_proyecto.txt`**: Documento que describe la estructura del proyecto.
- **`requirements.txt`**: Archivo que lista las dependencias del proyecto.

## Configuración

1. **Instalación de Dependencias**

   Primero, asegúrate de tener un entorno virtual activado, y luego instala las dependencias necesarias usando:

   ```bash
   pip install -r requirements.txt

## Configuración del Archivo .env

Crea un archivo .env en la raíz del proyecto con el siguiente contenido para almacenar tus credenciales de LinkedIn:

LINKEDIN_USERNAME=your_username
LINKEDIN_PASSWORD=your_password

 2. **Ejecutar el Script Principal**

Para iniciar el proceso de scraping, análisis de sentimientos y visualización, ejecuta:

python main.py
    
## Visualización

Una vez completado el análisis, se generarán gráficos interactivos con Plotly para visualizar los resultados de los sentimientos de las publicaciones.

## Disclaimer

El scraping de datos en LinkedIn está limitado fuera del uso del API oficial y puede estar sujeto a restricciones de uso. Se debe hacer de manera responsable y en cumplimiento con los términos de servicio de LinkedIn. Este proyecto es solo para fines educativos y de investigación.

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Por favor, abre un issue o una pull request si tienes sugerencias o mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Gracias por visitar el proyecto! Si tienes alguna pregunta, no dudes en abrir un issue.