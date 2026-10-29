from mysql.connector import Error
from conexion import obtener_conexion

class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado, id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def guardar(self):
        try:
            conexion = obtener_conexion()
            if not conexion: return None

            cursor = conexion.cursor()
            sql = """
                INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, estado)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (self.nombre, self.descripcion, self.fecha_inicio, self.fecha_fin, self.estado)
            cursor.execute(sql, valores)
            conexion.commit()
            self.id = cursor.lastrowid
            return self.id
        except Error as err:
            print(f"Error al guardar proyecto: {err}")
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
            cursor.execute("SELECT id, nombre, descripcion, fecha_inicio, fecha_fin, estado FROM proyectos")
            return cursor.fetchall()
        except Error as err:
            print(f"Error al listar proyectos: {err}")
            return []
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()