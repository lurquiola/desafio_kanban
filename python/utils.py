import csv
import app

def load_funcionarios_from_csv(file_path, funcionarios):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            funcionarios.create({
                'cedula': int(row['cedula']),
                'nombre': row['nombre'],
                'cargo': row['cargo'],
                'sueldo': int(row['sueldo']),
                'fecha_ingreso': row['fecha_ingreso']
            })

def load_recibos_from_csv(file_path, recibos):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print("Raw row data:", row)
            # cedula_funcionario = row['cedula_funcionario']
            # print("Cedula antes de convercion:", cedula_funcionario)
            # if cedula_funcionario:
            #     cedula_funcionario = int(cedula_funcionario)
            # else:
            #     cedula_funcionario = 0
            # print("Cedula despues", cedula_funcionario)
            recibos.create({
                'anio_mes': row['anio_mes'],
                'tipo_recibo': row['tipo_recibo'],
                'id_funcionario': int(row['id']),
                'nombre_empleador': row['nombre_empleador'],
                'detalle_recibo_id': int(row['detalle_recibo_id'])
            })

def load_detalle_recibo_from_csv(file_path, DetalleRecibo):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            DetalleRecibo.create({
                'detalle_recibo_id': int(row['id']),
                'tipo_concepto': row['tipo_concepto'],
                'cantidad': int(row['cantidad']),
                'monto': int(row['monto'])
            })

# Le paso una cedula y si esta en la base de datos me da 
# el id del funcionario para buscar en la tabla de recibos
# sino devuelve none y se debe de pedir una cedula valida
def get_funcionario_id_by_cedula(cedula: int, funcionario) -> int:
    for f in funcionario:
        if f.cedula == cedula:
            return f.id
    return None

def get_recibos_by_funcionario_id(funcionario_id: int, recibos):
    recibos_filtrados = []
    for recibo in recibos:
        recibo_data = recibo.read()
        # Verifica si el `id_funcionario` en el recibo coincide con el ID del funcionario proporcionado
        if recibo_data['id_funcionario'] == funcionario_id:
            # Si coincide, agrega el recibo a la lista de recibos filtrados
            recibos_filtrados.append(recibo)
    
    return recibos_filtrados

def cargar_base_de_datos():
    Funcionario = app.env['funcionarios']
    load_funcionarios_from_csv("data/cargar_funcionarios.csv", Funcionario)

    Detalle = app.env['detalle_recibo']
    load_detalle_recibo_from_csv("data/cargar_detalles.csv", Detalle)

    Recibos = app.env['recibos_sueldo']
    load_recibos_from_csv("data/cargar_recibos.csv", Recibos)

def eliminar_recibos():
    Funcionario = app.env['funcionarios']
    Recibos = app.env['recibos_sueldo']

    # listo todos los funcionarios
    todos_los_funcionarios = Funcionario.records()
    ci = int(input("Escriba CI del funcionario que se quiere eliminar los recibos: "))
    # Con esto busco el ID del funcionario con esta cedula
    id = get_funcionario_id_by_cedula(ci, todos_los_funcionarios)
    if id == None:
        print("Cedula invalida, intente de nuevo.")
    else:
        todos_los_recibos = Recibos.records()
        recibos_a_borrar = get_recibos_by_funcionario_id(id, todos_los_recibos)
        for elem in recibos_a_borrar:
            print("aca ", type(elem))
            elem.delete()

def actualizar_datos_funcionario():
    cedula = int(input("Ingresar cedula de identidad del funcionario que se quiere actualizar la informacion:"))
    nuevo_nombre = input("Ingresar actualizacion de nombre:")
    nuevo_cargo = input("Ingresar actualizacion de cargo:")

    Funcionarios = app.env['funcionarios']
    funcionarios = Funcionarios.records()
    aActualizar = None

    for funcionario in funcionarios:
        if funcionario.cedula == cedula:
            aActualizar = funcionario

        if aActualizar != None:
            aActualizar.update({
                'nombre': nuevo_nombre,
                'cargo': nuevo_cargo
            })
        else:
            print("Cedula invalida. No existe registro en la base de datos con esa cedula.")