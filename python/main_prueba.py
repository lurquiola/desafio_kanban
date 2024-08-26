import app
from utils import load_funcionarios_from_csv, load_recibos_from_csv, load_detalle_recibo_from_csv, get_funcionario_id_by_cedula, get_recibos_by_funcionario_id

# DB - {"funcionarios": [], "recibos_sueldo": [], "detalle_recibo": []}

Funcionario = app.env['funcionarios']
Recibos = app.env['recibos_sueldo']
"""

load_funcionarios_from_csv("data/cargar_funcionarios.csv", Funcionario)

Detalle = app.env['detalle_recibo']
load_detalle_recibo_from_csv("data/cargar_detalles.csv", Detalle)

Recibos = app.env['recibos_sueldo']
load_recibos_from_csv("data/cargar_recibos.csv", Recibos)
"""

# Con esto busco el ID del funcionario con esta cedula

todos_los_funcionarios = Funcionario.records()

#pedir input CI
ci = int(input("Escriba CI del funcionario que se quiere eliminar recibos: "))
id = get_funcionario_id_by_cedula(ci, todos_los_funcionarios)
if id == None:
    print("Cedula invalida, intente de nuevo.")
else:
    print(id)

print(todos_los_funcionarios)

todos_los_recibos = Recibos.records()

print(todos_los_recibos)

recibos_a_borrar = get_recibos_by_funcionario_id(id, todos_los_recibos)

print(recibos_a_borrar)

for elem in recibos_a_borrar:
    print("aca ", type(elem))
    elem.delete()

#rint(todos_recibos)
#funcionario_asociado = app.env['funcionarios'].browse(todos_recibos[0].id.id)

#Recibos.create({'cedula_funcionario': 12345678, 'tipo_recibo': 'vacaciones', 'anio_mes': '2024-08', 'nombre_empleador': 'kanban', 'detalle_recibo_id': 1})



"""
# Actualizar
cedula = "12345678"
nuevo_nombre = 'carlitos'
nuevo_cargo = 'prueba'

Funcionarios = app.env['funcionarios']
funcionarios = Funcionarios.records()
aActualizar = None

for funcionario in funcionarios:
        if funcionario.cedula == cedula:
             print("HOLA")
             aActualizar = funcionario

if aActualizar != None:
    print("aca")
    aActualizar.update({
        'nombre': nuevo_nombre,
        'cargo': nuevo_cargo
    })
"""