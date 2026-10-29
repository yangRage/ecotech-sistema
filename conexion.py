import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

#Cargar variables de entorno desde el archivo .env
load_dotenv()

def obtener_conexion():
    """Establece y retorna la conexión a la base de datos usando variables de entorno."""
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "ecotech_db")
        )
        return conexion
    except Error as err:
        print(f"Error de conexión con el servidor MySQL: {err}")
        return None