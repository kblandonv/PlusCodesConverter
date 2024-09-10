import googlemaps
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde las variables de entorno
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# Configurar el cliente de Google Maps con la clave de API
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# Lista de Plus Codes y nombres de las ubicaciones
plus_codes = [
    ("8FQ4+48 Bello, Antioquia", "Bello, Antioquia"),
    ("8CHW+XG Bello, Antioquia", "Bello, Antioquia"),
    ("8C8V+8V Bello, Antioquia", "Bello, Antioquia"),
    ("7CXR+WH Medellín, Antioquia", "Medellín, Antioquia"),
    ("7CRP+44 Medellín, Antioquia", "Medellín, Antioquia"),
    ("7CHJ+76 Medellín, Antioquia", "Medellín, Antioquia"),
    ("7C9M+QJ Medellín, Antioquia", "Medellín, Antioquia"),
    ("7C7P+HH Medellín, Antioquia", "Medellín, Antioquia"),
    ("7C4M+PG Medellín, Antioquia", "Medellín, Antioquia"),
    ("7C2J+5P Medellín, Antioquia", "Medellín, Antioquia"),
    ("6CWJ+V3 Medellín, Antioquia", "Medellín, Antioquia"),
    ("6CVH+5C Medellín, Antioquia", "Medellín, Antioquia"),
    ("6CQG+8P Medellín, Antioquia", "Medellín, Antioquia"),
    ("6CHF+XP Medellín, Antioquia", "Medellín, Antioquia"),
    ("6C7C+3Q Medellín, Antioquia", "Medellín, Antioquia"),
    ("5CV9+G7 Medellín, Antioquia", "Medellín, Antioquia"),
    ("5CP7+JR Envigado, Antioquia", "Envigado, Antioquia"),
    ("5CP7+JR Envigado, Antioquia", "Envigado, Antioquia"),
    ("5CF3+V5 Envigado, Antioquia", "Envigado, Antioquia"),
    ("597V+7J Itagüi, Antioquia", "Itagüi, Antioquia"),
    ("594M+X7 Sabaneta, Antioquia", "Sabaneta, Antioquia"),
    ("593F+3C Sabaneta, Antioquia", "Sabaneta, Antioquia"),
]

def get_coordinates(plus_code):
    """
    Obtiene las coordenadas (latitud y longitud) a partir de un código Plus.

    Args:
        plus_code (str): El código Plus que se desea geocodificar.

    Returns:
        tuple: Una tupla con la latitud y longitud (lat, lng) si se encuentra el código Plus,
               de lo contrario, devuelve (None, None).

    Raises:
        Exception: Si ocurre un error durante el proceso de geocodificación.
    """
    try:
        # Usar la función geocode() de la biblioteca googlemaps
        result = gmaps.geocode(plus_code)
        if result:
            location = result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"No se encontraron resultados para {plus_code}")
            return None, None
    except Exception as e:
        print(f"Error al procesar {plus_code}: {str(e)}")
        return None, None

def generate_kml(coordinates_list):
    """
    Genera un archivo KML a partir de una lista de coordenadas.
    Args:
        coordinates_list (list): Lista de tuplas, donde cada tupla contiene 
                                 el nombre (str), latitud (float) y longitud (float) 
                                 de una ubicación.
    Returns:
        None: El archivo KML se guarda en el directorio actual con el nombre 'ubicaciones.kml'.
    """
    kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, "Document")
    name = ET.SubElement(document, "name")
    name.text = "Ubicaciones Plus Codes"

    for name, lat, lng in coordinates_list:
        placemark = ET.SubElement(document, "Placemark")
        place_name = ET.SubElement(placemark, "name")
        place_name.text = name

        point = ET.SubElement(placemark, "Point")
        coordinates = ET.SubElement(point, "coordinates")
        coordinates.text = f"{lng},{lat},0"

    tree = ET.ElementTree(kml)
    tree.write("ubicaciones.kml", xml_declaration=True, encoding='utf-8')

coordinates_list = []

for plus_code, place_name in plus_codes:
    lat, lng = get_coordinates(plus_code)
    if lat is not None and lng is not None:
        coordinates_list.append((place_name, lat, lng))
    else:
        print(f"No se pudo obtener coordenadas para: {plus_code}")

generate_kml(coordinates_list)

print("Archivo KML generado con éxito: ubicaciones.kml")