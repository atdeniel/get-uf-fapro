
from functools import wraps
from typing import Callable

from fastapi import HTTPException
from fastapi.responses import JSONResponse


def handle_response(func: Callable):
    """
    Un decorador diseñado para envolver funciones asincrónicas en servicios web, 
    principalmente usado para manejar las respuestas y excepciones de manera estandarizada.

    Captura el resultado de la función asincrónica decorada y lo devuelve como una respuesta
    JSON con un código de estado HTTP 200. Maneja específicamente las excepciones ValueError
    y Exception, devolviendo respuestas de error con códigos de estado HTTP 400 y 500,
    respectivamente, y un detalle del error.

    Parameters:
    - func (Callable): La función asincrónica a decorar, que se espera devuelva un resultado
      que pueda ser serializado en JSON.

    Returns:
    - Callable: Una función wrapper asincrónica que puede ser llamada con los mismos argumentos
      que la función original. La función wrapper maneja la ejecución de la función decorada,
      captura y maneja excepciones, y estandariza la respuesta HTTP.

    Raises:
    - HTTPException: Se lanza con un código de estado 400 para errores de validación (ValueError)
      o con un código de estado 500 para cualquier otro tipo de error excepcional.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            return JSONResponse(status_code=200, content=result)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return wrapper
