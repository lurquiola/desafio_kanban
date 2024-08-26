# Pago de sueldos
import app
from utils import load_funcionarios_from_csv, load_recibos_from_csv, load_detalle_recibo_from_csv

print("Bienvenido al sistema de pago de sueldos de Kanban")

while True:
  print("\n--- Menú de Opciones ---")
  print("1) Cargar datos desde archivos CSV")
  print("2) Dar de alta un nuevo funcionario")
  print("3) Agregar recibo de sueldo")
  print("4) Modificar nombre y cargo de un funcionario")
  print("5) Salir")
  
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
      print("Cargando datos...")

      Funcionario = app.env['funcionarios']
      load_funcionarios_from_csv("data/cargar_funcionarios.csv", Funcionario)

      Detalle = app.env['detalle_recibo']
      load_detalle_recibo_from_csv("data/cargar_detalles.csv", Detalle)

      Recibos = app.env['recibos_sueldo']
      load_recibos_from_csv("data/cargar_recibos.csv", Recibos)

  elif opcion == '2':
      print("Dando de alta un funcionario nuevo ...")

      Funcionario = app.env['funcionarios']
      cedula = input("Ingresar cedula de identidad del funcionario:")
      nombre = input("Ingresar nombre:")
      cargo = input("Ingresar cargo:")
      sueldo = input("Ingresar sueldo:")
      fecha_ingreso = input("Ingresar fecha de ingreso:")
      funcionario = Funcionario.create({'nombre': nombre, 'sueldo': sueldo, 'cargo': cargo, 'cedula': cedula, 'fecha_ingreso': fecha_ingreso})
  elif opcion == '3':
      print("Agrego recibo.")
      #agregar_recibo()
  elif opcion == '4':
      print("Actualizar informacion de funcionario.")
      cedula = input("Ingresar cedula de identidad del funcionario que se quiere actualizar la informacion:")
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
  elif opcion == '5':
      print("Saliendo del programa...")
      break
  else:
      print("Opción no válida, intente nuevamente.")

print('\napp.env almacena el entorno de la aplicacion, desde donde se puede acceder a la definición de los modelos de la siguiente forma:')
# Car = app.env['car_car']


funcionario = Funcionario.create({'nombre': 'Juan Pérez', 'sueldo': '30000', 'cargo': 'Administrativo', 'cedula': 12345678, 'fecha_ingreso': '2024-08-21'})
print(funcionario.read())

all_funcionarios = app.env['funcionarios'].records()
for funcionario in all_funcionarios:
    print(funcionario.read())


# recibos = []
# for i in range(1, 5):
#     recibos.append(ReciboSueldo.create({'funcionario_id': funcionario.id, 'monto': 1000 * i, 'fecha_pago': '2024-08-21'}))
# print(recibos)


# print('\nEl método create recibe un diccionario de valores y retorna una instancia del modelo para el registro que acaba de crear:')
# car = Car.create({'color': 'Rojo', 'brand': 'Hyundai'})
# print(car)
# print(car.seats_count)

# seats = []
# print(seats)
# for i in range(1, 5):
#   seats.append(app.env['car_seat'].create({'car_id': car.id}))
#   print(seats)

# print('\nSe puede acceder a las columnas de un modelo como atributos e incluso actualizarlas:')
# car.seats_count = len(seats)
# print(car.seats_count)

# print('\nEl método records retorna todos los registros existentes para el modelo indicado como una lista de instancias:')
# all_seats = app.env['car_seat'].records()
# print(all_seats)

# print('\nEl método read retorna los valores de todas las columnas de un registro como un diccionario:')
# for seat in all_seats:
#   print(seat.read())

# print('\nEl método browse retorna el regsitro del modelo según el ID recibido - también puede recibir lista de IDs, en cuyo caso retorna una lista de registros:')
# car_again = Car.browse(all_seats[0].car_id.id)
# print(car_again)
# print(car.read() == car_again.read())
# del car_again

# print('\nEl método update recibe un diccionario de valores y actualiza las columnas del registro con los nuevos valores:')
# print(car.read())
# car.update({'color': 'Azul', 'open_ceiling': True})
# print(car.read())

# print('\nEl método delete elimina el registro en base de datos:')
# for seat in all_seats:
#   seat.delete()
# car.delete()
# print(Car.records())
# print(app.env['car_seat'].records())