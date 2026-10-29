import sys
from database import crear_tablas, limpiar_tablas
from departamento import Departamento
from empleado import Empleado
from proyecto import Proyecto

def ejecutar_demostracion_sistema():
    
    print("ECOTECH SOLUTIONS - SISTEMA DE GESTIÓN DE EMPLEADOS")
    
    # 1. Preparar Base de Datos
    crear_tablas()
    limpiar_tablas()

    # 2.CREATE
    print("\n1.CREATE (Registro de Entidades)")
    dpto_ti = Departamento("Tecnologías de la Información")
    id_dpto = dpto_ti.guardar()
    print(f"Departamento registrado con ID: {id_dpto}")

    empleado1 = Empleado(
        nombre="Roberto Pérez",
        email="roberto.perez@ecotech.cl",
        password_hash="asale65",
        fecha_inicio="2025-06-03",
        salario=1200000.00,
        direccion="Pasaje El Tranque 14, Puerto Montt",
        telefono="+56912345679",
        departamento_id=id_dpto
    )
    id_emp = empleado1.guardar()

    proyecto1 = Proyecto(
        nombre="Desarrollo Plataforma Web",
        descripcion="Sistema web para clientes EcoTech.",
        fecha_inicio="2026-04-01",
        fecha_fin="2026-12-31",
        estado="En progreso"
    )
    id_proy = proyecto1.guardar()
    print(f"Proyecto registrado con ID: {id_proy}")

    #3.READ
    print("\n2.READ (Consulta de Datos)")
    print("Empleados en el Departamento de TI:")
    empleados = Empleado.listar_por_departamento(id_dpto)
    for emp in empleados:
        print(f"  [ID: {emp[0]}] Nombre: {emp[1]} | Email: {emp[2]} | Salario: ${emp[3]:,.2f}")

    #4.UPDATE
    print("\n3. UPDATE (Modificación de Registros)")
    empleado1.actualizar(
        nuevo_salario=1450000.00, 
        nueva_direccion="Av. Austral 456, Puerto Montt",
        nuevo_telefono="+56998765432"
    )

    #5.DELETE
    print("\n4. DELETE (Eliminación de Registros)")
    empleado1.eliminar()

    print("Verificación de empleados tras la eliminación:")
    empleados_restantes = Empleado.listar_por_departamento(id_dpto)
    if not empleados_restantes:
        print("La lista de empleados se encuentra vacía. Registro eliminado exitosamente.")

    #6. Prueba de Validación de Errores (Entrada no válida)
    print("\n5. PRUEBA DE MANEJO DE EXCEPCIONES Y VALIDACIÓN")
    empleado_invalido = Empleado(
        nombre="A", # Nombre demasiado corto
        email="correo_invalido", # Sin formato email
        password_hash="123",
        fecha_inicio="2026-01-01",
        salario=-500000, # Salario negativo
        direccion="",
        telefono="",
        departamento_id=id_dpto
    )
    empleado_invalido.guardar()

    print("PRUEBA COMPLETA DE SISTEMA Y VALIDACIONES FINALIZADA")


if __name__ == "__main__":
    ejecutar_demostracion_sistema()