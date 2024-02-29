import re
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Query

from services.sii_service import sii_service
from utils.api_handler import handle_response

router = APIRouter()

def validate_date(date_str: str) -> datetime:
    """
    Valida si una cadena de texto representa una fecha válida en el formato 'dd-mm-yyyy'.

    La fecha debe cumplir con los siguientes criterios:
    - Estar en el formato 'dd-mm-yyyy'.
    - Ser posterior al 01-01-2013.
    - Ser anterior o igual a la fecha actual.

    Parameters:
    - date_str (str): La cadena de texto que representa la fecha a validar.

    Returns:
    - datetime: Un objeto datetime correspondiente a la fecha validada.

    Raises:
    - ValueError: Si la fecha no está en el formato 'dd-mm-yyyy'.
    - ValueError: Si la fecha es anterior o igual al 01-01-2013.
    - ValueError: Si la fecha es posterior a la fecha actual.
    """

    if not re.match(r"\d{2}-\d{2}-\d{4}", date_str):
        raise ValueError('La fecha debe estar en formato dd-mm-yyyy.')
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    if date_obj <= datetime(2013, 1, 1):
        raise ValueError('La fecha debe ser mayor a 01-01-2013.')
    if date_obj > datetime.now():
        raise ValueError('La fecha debe ser menor a la actual.')
    return date_obj


@router.get('/uf')
@handle_response
async def get_uf(date: Annotated[
    str, 
    Query(...,
        example='19-03-2014',
        description='Fecha en formato dd-mm-yyyy',
        min_length=10,
        max_length=10,
        regex=r"\d{2}-\d{2}-\d{4}",
        title="Fecha"
    )]) -> dict:
    """
    Asíncronamente obtiene el valor de la Unidad de Fomento (UF) para una fecha dada.

    Parameters:
    - date (Annotated[str, Query]): Una cadena que representa la fecha para la cual se desea
      obtener el valor de la UF. Debe estar en el formato 'dd-mm-yyyy'. Esta fecha es validada
      para asegurar que sigue el formato correcto y que es una fecha válida dentro del rango
      permitido.

    Returns:
    - dict: Un diccionario que contiene la fecha consultada y el valor de la UF correspondiente.
      Ejemplo: {'date': '19-03-2014', 'uf_value': 24000.52}

    Raises:
    - ValueError: Si la fecha no está en el formato 'dd-mm-yyyy', es anterior al 01-01-2013, o es
      posterior a la fecha actual.
    - Exception: Si ocurre un error al consultar el valor de la UF en el servicio del SII.
    """

    validate_date(date)
    sii_service_response = sii_service.get_uf_by_date(date)
    (status, value) = tuple(sii_service_response.values())

    if not status:
        raise Exception('Ocurrio un error en consultar el valor de la UF.')

    return {'date':date, 'uf_value': value}




