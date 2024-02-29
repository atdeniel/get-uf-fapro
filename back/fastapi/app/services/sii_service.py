from config.settings import setting
from utils.beautiful_soup import scrape_website

class SiiService:
    """
    Un servicio para interactuar con el Servicio de Impuestos Internos (SII) para obtener
    datos financieros, por ejemplo los valores de la Unidad de Fomento (UF).
    """

    def get_uf_by_date(self, date_str: str) -> dict:
        """
        Obtiene el valor de la Unidad de Fomento (UF) para una fecha específica a partir de los datos
        del SII. El método realiza una solicitud a una URL específica del SII, que varía según el año
        de la fecha proporcionada. Utiliza scraping web para extraer el valor de la UF de la respuesta.

        Parameters:
        - date_str (str): La fecha para la cual se desea obtener el valor de la UF, en formato 'dd-mm-yyyy'.

        Returns:
        - dict: Un diccionario con dos claves: 'status' y 'value'. 'status' es un booleano que indica si
          la operación fue exitosa, y 'value' es el valor de la UF para la fecha dada si la operación fue
          exitosa, de lo contrario es None.
        """

        date_split = date_str.split('-')
        year = date_split[2]
        url = setting.get_sii_uf_year_url(year)
        date_keys = ['day', 'month', 'year']
        date_dict = dict(zip(date_keys, date_split))
        scrape_response = scrape_website(url, 'sii_soup', 'find_value_for_day', date_dict)
        (status, value) = tuple(scrape_response.values())
        return {'status': status, 'value': value}
    
sii_service = SiiService()
