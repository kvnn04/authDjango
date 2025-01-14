from abc import ABC, abstractmethod
from datetime import timezone, timedelta, datetime
from ..config.variablesEntorno import ConfigEnv
from jwt import encode

class AbsEncode(ABC):

    @staticmethod
    @abstractmethod
    def encode():
        pass

class EncodeObject(AbsEncode):
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia
    
    @staticmethod
    def encode(diccionario: dict)-> str:
        condicion = isinstance(diccionario, (dict))
        if not condicion:
            raise ValueError(message='Espera un diccionario')

        try:
            diccionario['exp'] = datetime.now(timezone.utc) + timedelta(hours=1)
            diccionario['iat'] = datetime.now(timezone.utc)
            payload = encode(payload=diccionario, key=ConfigEnv.SECRET_KEY.value, algorithm=['HS256'])
            print(payload)
            return payload
        except Exception as e:
            print(f"Error: {e}")
            raise ValueError("Ocurrió un error al generar el token")
    