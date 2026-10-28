import sys
from database import crear_tablas, limpiar_tablas
from departamento import Departamento
from empleado import Empleado
from proyecto import Proyecto

# 1. Crear las tablas y vaciar datos antiguos para la prueba
crear_tablas()
limpiar_tablas()  # <--- Esta llamada vacía la BD antes de insertar

# 2. Registrar e imprimir Departamento
dpto_ti = Departamento("Tecnologías de la Información")
id_dpto_ti = dpto_ti.guardar()
print(f"Departamento registrado con ID: {id_dpto_ti}")

print("\nDepartamentos registrados:")
for dpto in Departamento.listar():
    print(dpto)

# 3. Registrar e imprimir Empleado
empleado1 = Empleado(
    nombre="Roberto Pérez",
    email="roberto.perez@ecotech.cl",
    password_hash="hashed_password",
    fecha_inicio="2024-06-01",
    salario=1200000.00,
    direccion="Calle Falsa 123, Puerto Montt",
    telefono="+56 9 1234 5679",
    departamento_id=id_dpto_ti
)
id_emp = empleado1.guardar()
print(f"\nEmpleado registrado con ID: {id_emp}")

print("Empleados en el departamento:")
for emp in Empleado.listar_por_departamento(id_dpto_ti):
    print(emp)

# 4. Registrar e imprimir Proyecto
proyecto1 = Proyecto(
    nombre="Desarrollo de Plataforma Web",
    descripcion="Proyecto para desarrollar una nueva plataforma web para clientes.",
    fecha_inicio="2026-04-01",
    fecha_fin="2026-12-31",
    estado="En progreso"
)
id_proy = proyecto1.guardar()
print(f"\nProyecto registrado con ID: {id_proy}")

print("\nProyectos registrados:")
for proy in Proyecto.listar():
    print(proy)