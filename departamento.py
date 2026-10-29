from mysql.connector import Error
from conexion import obtener_conexion

class Departamento:
    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre

    def guardar(self):
        try:
            if not self.nombre or len(self.nombre.strip()) < 2:
                raise ValueError("El nombre del departamento no puede estar vacío.")

            conexion = obtener_conexion()
            if not conexion: return None

            cursor = conexion.cursor()
            sql = "INSERT INTO departamentos (nombre) VALUES (%s)"
            cursor.execute(sql, (self.nombre,))
            conexion.commit()
            self.id = cursor.lastrowid
            return self.id
        except (ValueError, Error) as err:
            print(f"Error en Departamento.guardar: {err}")
            return None
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    @staticmethod
    def listar():
        try:
            conexion = obtener_conexion()
            if not conexion: return []

            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM departamentos")
            departamentos = cursor.fetchall()
            return departamentos
        except Error as err:
            print(f"Error al listar departamentos: {err}")
            return []
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()