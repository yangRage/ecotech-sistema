from mysql.connector import Error
from conexion import obtener_conexion

def crear_tablas():
    #Crea las tablas si no existen en MySQL.
    conexion = obtener_conexion()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                password_hash VARCHAR(256) NOT NULL,
                fecha_inicio DATE NOT NULL,
                salario DECIMAL(10, 2) NOT NULL,
                direccion VARCHAR(200),
                telefono VARCHAR(20),
                departamento_id INT,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE SET NULL
            ) ENGINE=InnoDB
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS proyectos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion VARCHAR(255),
                fecha_inicio DATE,
                fecha_fin DATE,
                estado VARCHAR(50)
            ) ENGINE=InnoDB
        """)
        conexion.commit()
        print("Tablas del sistema EcoTech verificadas correctamente.")
    except Error as err:
        print(f"Error al crear la estructura de tablas: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def limpiar_tablas():
    #Elimina y recrea las tablas para asegurar el esquema correcto en pruebas.
    conexion = obtener_conexion()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("DROP TABLE IF EXISTS empleados")
        cursor.execute("DROP TABLE IF EXISTS proyectos")
        cursor.execute("DROP TABLE IF EXISTS departamentos")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        conexion.commit()
        
        # Recrear la estructura limpia
        crear_tablas()
        print("Base de datos reiniciada para pruebas.")
    except Error as err:
        print(f"Error al limpiar las tablas: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()