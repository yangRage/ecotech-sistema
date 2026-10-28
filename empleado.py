from conexion import obtener_conexion
from usuario import Usuario

class Empleado(Usuario):
    def __init__(self,nombre, email, password_hash, fecha_inicio, salario, direccion, telefono, departamento_id):
        #Atributos heredados por la clase Usuario
        super().__init__(nombre, email, password_hash)
        
        #Atributos específicos de la clase Empleado
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.direccion = direccion
        self.telefono = telefono
        self.departamento_id = departamento_id
        
    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO empleados (nombre, email, password_hash, fecha_inicio, salario, direccion, telefono, departamento_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (self.nombre, self.email, self.password_hash, self.fecha_inicio, self.salario, self.direccion, self.telefono, self.departamento_id)
        cursor.execute(sql, valores)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()

        return self.id
    
    @staticmethod
    def listar_por_departamento(departamento_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            SELECT id, nombre, email, salario
            FROM empleados
            WHERE departamento_id = %s
        """
        cursor.execute(sql, (departamento_id,))
        empleados = cursor.fetchall()
        cursor.close()
        conexion.close()

        return empleados