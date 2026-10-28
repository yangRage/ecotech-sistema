from conexion import obtener_conexion

class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado):
      self.id = None
      self.nombre = nombre
      self.descripcion = descripcion
      self.fecha_inicio = fecha_inicio
      self.fecha_fin = fecha_fin
      self.estado = estado
    
    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO proyectos (nombre, descripcion, fecha_inicio)
            VALUES (%s, %s, %s)
        """
        valores = (self.nombre, self.descripcion, self.fecha_inicio)
        cursor.execute(sql, valores)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()

        return self.id
    
    @staticmethod
    def listar():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proyectos")

        proyectos = cursor.fetchall()
        cursor.close()
        conexion.close()

        return proyectos