from bs4 import BeautifulSoup

def find_value_for_day(soup: BeautifulSoup, parameters: dict) -> str:
    """
    Busca y extrae el valor correspondiente a un día específico de un mes dentro de una tabla
    en una página web, utilizando BeautifulSoup para analizar el contenido HTML.

    Parameters:
    - soup (BeautifulSoup): El objeto BeautifulSoup que representa el contenido HTML de la
      página web que se está analizando.
    - parameters (dict): Un diccionario que debe contener minimo las claves 'month' y 'day', donde
      'month' es el mes (1-12) y 'day' es el día del mes para el cual se busca el valor.

    Returns:
    - str: El valor encontrado para el día y mes especificados. Si los parámetros son inválidos o
      si no se encuentra el valor, se devuelve un mensaje de error correspondiente.
    """

    month_param = int(parameters.get('month', 0))
    day_param = int(parameters.get('day', 0))
    if month_param == 0 and day_param == 0:
        return 'Invalid month or day parameters'

    table = soup.find('table', {'id': 'table_export'})
    tbody = table.find('tbody')

    for row in tbody.find_all('tr'):
        day_row = int(row.find('th').text)
        if day_row == day_param:
            cells = row.find_all('td')
            value = cells[month_param - 1].text.strip()
            return value

    return 'Value not found'