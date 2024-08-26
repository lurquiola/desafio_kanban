import csv

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