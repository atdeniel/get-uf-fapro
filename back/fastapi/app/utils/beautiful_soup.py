import importlib
import requests

from bs4 import BeautifulSoup

def scrape_website(url: str , soup_type: str , soup_function: str, parameters: dict) -> dict:
    """
    Realiza scraping en una página web especificada para extraer información utilizando
    BeautifulSoup y una función de scraping personalizada.

    Intenta importar dinámicamente un módulo y una función de scraping basada en los
    parámetros proporcionados, ejecuta la función de scraping con los parámetros dados y
    devuelve el resultado.

    Parameters:
    - url (str): La URL de la página web desde la cual se va a hacer scraping.
    - soup_type (str): El nombre del módulo de scraping dentro de 'utils.scrapping_soup'
      que contiene la función de scraping a utilizar. Ejemplo: sii_soup
    - soup_function (str): El nombre de la función de scraping dentro del módulo especificado
      que se va a ejecutar. Ejemplo: find_value_for_day
    - parameters (dict): Un diccionario de parámetros que se pasará a la función de scraping.

    Returns:
    - dict: Un diccionario con dos claves: 'status' y 'value'. 'status' es un booleano que indica
      si la operación de scraping fue exitosa. 'value' contiene el resultado del scraping si
      'status' es True, o un mensaje de error si 'status' es False.
    """
    try:
        module = importlib.import_module(f'utils.scrapping_soup.{soup_type}')
        function = getattr(module, soup_function)
    except ModuleNotFoundError:
        return {
            'status': False,
            'value': f'El módulo especificado para el tipo {soup_type} no se encontró.'
            }
    except AttributeError:
        return {
            'status': False,
            'value': f'La función {soup_function} no se encontró en el módulo {soup_type}.'
            }

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        value = function(soup, parameters)
        return {
            'status': True,
            'value': value
            }
    else:
        return {
            'status': False,
            'value': 'No se pudo acceder a la página para hacer scraping.'
            }

