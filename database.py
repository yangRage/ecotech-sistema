from conexion import obtener_conexion

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla departamentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB
    """)
    
    # Crear tabla empleados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password_hash VARCHAR(200) NOT NULL,
            fecha_inicio DATE NOT NULL,
            salario DECIMAL(10, 2),
            direccion VARCHAR(200),
            telefono VARCHAR(20),
            departamento_id INT,
            FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
        ) ENGINE=InnoDB
    """)
    
    # Crear tabla proyectos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proyectos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            descripcion VARCHAR(255),
            fecha_inicio DATE
        ) ENGINE=InnoDB
    """)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tablas de EcoTech creadas exitosamente.")

def limpiar_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Eliminar tablas si existen
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")  # Desactivar temporalmente las comprobaciones de clave foránea
    cursor.execute("TRUNCATE TABLE empleados")
    cursor.execute("TRUNCATE TABLE departamentos")
    cursor.execute("TRUNCATE TABLE proyectos")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")  # Reactivar las comprobaciones de clave foránea
    
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tablas de EcoTech eliminadas exitosamente.")    