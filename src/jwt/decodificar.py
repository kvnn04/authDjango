from abc import ABC, abstractmethod
from jwt import decode
from ..config.variablesEntorno import ConfigEnv


class AbsDecode(ABC):

    @staticmethod
    @abstractmethod
    def decode():
        pass

class DecodeObject(AbsDecode):
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia
    
    @staticmethod
    def decode(token: str) -> dict:
        condicion = isinstance(token, (str))
        if not condicion:
            raise ValueError(message='Solo acepta strings')
        
        try:
            decodeToken = decode(jwt=token, key=ConfigEnv.SECRET_KEY.value, algorithms=['HS256'])
            return decodeToken
        except Exception as e:
            print(e)
            raise ValueError('Error al decodificar el token')
        
    @staticmethod
    def decodeForDb(token: str) -> dict:
        condicion = isinstance(token, (str))
        if not condicion:
            raise ValueError(message='Solo acepta strings')
        
        try:
            decodeToken = decode(jwt=token, key=ConfigEnv.SECRET_KEY_FOR_ENCODE_DB.value, algorithms=['HS256'])
            return decodeToken
        except Exception as e:
            print(e)
            raise ValueError('Error al decodificar el token')