import app
from utils import load_funcionarios_from_csv, load_recibos_from_csv, load_detalle_recibo_from_csv

# DB - {"funcionarios": [], "recibos_sueldo": [], "detalle_recibo": []}
"""
Funcionario = app.env['funcionarios']
load_funcionarios_from_csv("data/cargar_funcionarios.csv", Funcionario)

Detalle = app.env['detalle_recibo']
load_detalle_recibo_from_csv("data/cargar_detalles.csv", Detalle)

Recibos = app.env['recibos_sueldo']
load_recibos_from_csv("data/cargar_recibos.csv", Recibos)
"""

all_funcionarios = app.env['funcionarios'].records()

#todos_recibos = app.env['recibos_sueldo'].records()
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