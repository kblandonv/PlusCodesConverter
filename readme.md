# Generador de KML a partir de Plus Codes

Este proyecto utiliza la API de Google Maps para convertir Plus Codes en coordenadas geográficas y generar un archivo KML con estos datos.

## Requisitos

- Python 3.x
- Paquetes Python: `googlemaps`, `python-dotenv`

## Instalación

1. **Clona este repositorio**:

   ```bash
   git clone 

2. **Instala las dependencias**:

    ```bash
    pip install googlemaps python-dotenv

3. **Configura tu clave de API de Google Maps**:

Crea un archivo .env en el mismo directorio que tu script.

Agrega tu clave de API de Google Maps en el archivo .env con el siguiente formato:

    ```
    GOOGLE_MAPS_API_KEY=tu_clave_de_api_aqui

## Uso
Ejecuta el script:

    ```python
    ubicaciones.py

Esto generará un archivo ubicaciones.kml en el directorio actual.

## Descripción del Código
Carga de Variables de Entorno: Usa python-dotenv para cargar la clave de API de Google Maps desde un archivo .env.
Geocodificación de Plus Codes: La función get_coordinates utiliza la API de Google Maps para convertir Plus Codes en coordenadas (latitud y longitud).
Generación de Archivo KML: La función generate_kml crea un archivo KML a partir de una lista de ubicaciones con sus coordenadas.

Ejemplo de Plus Codes:

"8FQ4+48 Bello, Antioquia"
"7CXR+WH Medellín, Antioquia"
"5CP7+JR Envigado, Antioquia"

## Archivos Generados
ubicaciones.kml: Archivo KML con la información de las ubicaciones geocodificadas.

## Contribuciones
Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y realiza un pull request con tus mejoras.


## Contacto
Para más información, puedes contactar a kblandonv@unal.edu.co
