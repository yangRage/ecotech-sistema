from conexion import obtener_conexion

class Departamento:
    def __init__(self, nombre):
        self.id = None
        self.nombre = nombre
        
    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        sql = """
        INSERT INTO departamentos (nombre) VALUES (%s)
        """
        valores = (self.nombre,)
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
        cursor.execute("SELECT * FROM departamentos")
        
        departamentos = cursor.fetchall()
        cursor.close()
        conexion.close()
        
        return departamentos