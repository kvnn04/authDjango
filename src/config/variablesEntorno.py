from dotenv import load_dotenv
from os import getenv
from enum import Enum

# Cargar variables de entorno desde el archivo .env
load_dotenv('data.env')

print(getenv('SECRET_KEY'))

def raiseError(message: str):
    raise ValueError(message)

class ConfigEnv(Enum):
    SECRET_KEY = getenv('SECRET_KEY') if getenv('SECRET_KEY') else raiseError('No estan las credeciales') 
    # SECRET_KEY_FOR_ENCODE_DB=getenv('SECRET_KEY_FOR_ENCODE_DB') 

# print(type(ConfigEnv.SECRET_KEY.value)) // tipo str
# print(type(ConfigEnv.SECRET_KEY)) // tipo ConfigEnv