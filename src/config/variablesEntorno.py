from dotenv import load_dotenv
from os import getenv
from enum import Enum

# Cargar variables de entorno desde el archivo .env
load_dotenv('data.env')

print(getenv('SECRET_KEY'))

class ConfigEnv(Enum):
    SECRET_KEY = getenv('SECRET_KEY')
    SECRET_KEY_FOR_ENCODE_DB=getenv('SECRET_KEY_FOR_ENCODE_DB')

# print(type(ConfigEnv.SECRET_KEY.value)) // tipo str
# print(type(ConfigEnv.SECRET_KEY)) // tipo ConfigEnv