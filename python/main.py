# Pago de sueldos
import app
import utils

print("Bienvenido al sistema de pago de sueldos de Kanban")

while True:
    print("\n--- Menú de Opciones ---")
    print("1) Cargar datos desde archivos CSV")
    print("2) Eliminar recibos de sueldo de un funcionario a partir de CI")
    print("3) Modificar nombre y cargo de un funcionario")
    print("4) Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Cargando datos...")
        utils.cargar_base_de_datos()
    elif opcion == '2':
        utils.eliminar_recibos()
    elif opcion == '3':
        utils.actualizar_datos_funcionario()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente nuevamente.")
