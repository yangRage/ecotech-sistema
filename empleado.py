import mysql.connector
from mysql.connector import Error
from conexion import obtener_conexion
from usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, email, password_hash, fecha_inicio, salario, direccion, telefono, departamento_id, id=None):
        # Atributos heredados de la clase Usuario
        super().__init__(nombre, email, password_hash)
        
        # Atributos específicos de la clase Empleado
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.direccion = direccion
        self.telefono = telefono
        self.departamento_id = departamento_id

    #Validar entrada
    def validar_datos(self):
        if not self.nombre or len(self.nombre.strip()) < 2:
            raise ValueError("El nombre del empleado es obligatorio y debe tener al menos 2 caracteres.")
        if "@" not in self.email or len(self.email.strip()) < 5:
            raise ValueError("El email del empleado es obligatorio y debe ser válido.")
        if self.salario < 0:
            raise ValueError("El salario del empleado no puede ser negativo.")
        return True

    # Guardar
    def guardar(self):
        try:
            self.validar_datos()
            conexion = obtener_conexion()
            if not conexion: 
                return None
            cursor = conexion.cursor()

            sql = """
                INSERT INTO empleados (nombre, email, password_hash, fecha_inicio, salario, direccion, telefono, departamento_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (self.nombre, self.email, self.password_hash, self.fecha_inicio, self.salario, self.direccion, self.telefono, self.departamento_id)
            cursor.execute(sql, valores)
            conexion.commit()
            self.id = cursor.lastrowid
            print(f"Empleado {self.nombre} registrado con ID: {self.id}")
            return self.id
        except ValueError as value_err:
            print(f"Validación fallida: {value_err}")
            return None
        except Error as mysql_err:
            print(f"Error al registrar en MySQL: {mysql_err}")
            return None
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    #Leer
    @staticmethod
    def listar_por_departamento(departamento_id):
        try:
            conexion = obtener_conexion()
            if not conexion: 
                return []
            cursor = conexion.cursor()
            
            sql = """
                SELECT id, nombre, email, salario
                FROM empleados
                WHERE departamento_id = %s
            """
            cursor.execute(sql, (departamento_id,))
            empleados = cursor.fetchall()
            return empleados
        except Error as mysql_err:
            print(f"Error al consultar empleados: {mysql_err}")
            return []
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    #Actualizar
    def actualizar(self, nuevo_salario, nueva_direccion, nuevo_telefono):
        try:
            if nuevo_salario < 0:
                raise ValueError("El salario no puede ser negativo.")
            conexion = obtener_conexion()
            if not conexion: 
                return False
            cursor = conexion.cursor()

            sql = """
                UPDATE empleados
                SET salario = %s, direccion = %s, telefono = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_salario, nueva_direccion, nuevo_telefono, self.id))
            conexion.commit()
            self.salario = nuevo_salario
            self.direccion = nueva_direccion
            self.telefono = nuevo_telefono
            print(f"Empleado {self.nombre} actualizado: Salario=${self.salario:,.2f}, Dirección={self.direccion}, Teléfono={self.telefono}")
            return True
        except ValueError as value_err:
            print(f"Validación fallida: {value_err}")
            return False
        except Error as mysql_err:
            print(f"Error al actualizar el empleado: {mysql_err}")
            return False
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    #Borrar
    def eliminar(self):
        try:
            if not self.id:
                raise ValueError("El empleado no tiene un ID válido para eliminar.")

            conexion = obtener_conexion()
            if not conexion: 
                return False
            cursor = conexion.cursor()

            sql = "DELETE FROM empleados WHERE id = %s"
            cursor.execute(sql, (self.id,))
            conexion.commit()
            print(f"Empleado {self.nombre} con ID {self.id} eliminado correctamente.")
            return True
        except ValueError as value_err:
            print(f"x Validación fallida: {value_err}")
            return False
        except Error as mysql_err:
            print(f"Error al eliminar el empleado: {mysql_err}")
            return False
        finally:
            if 'conexion' in locals() and conexion and conexion.is_connected():
                cursor.close()
                conexion.close()