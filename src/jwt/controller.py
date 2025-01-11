from abc import ABC, abstractmethod
from .codificar import EncodeObject
from .decodificar import DecodeObject

class AbstraccionJWT(ABC):

    @staticmethod
    @abstractmethod
    def crearObjectEncode():
        pass
    
    @staticmethod
    @abstractmethod
    def crearObjectDecode():
        pass

class ControllerJwt(AbstraccionJWT):
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

    @staticmethod
    def crearObjectEncode():
        return EncodeObject

    @staticmethod
    def crearObjectDecode():
        return DecodeObject