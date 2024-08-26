from app import models, columns

# Funcionarios: cedula, nombre, cargo, sueldo, fechaIngreso

class Funcionarios(models.Model):
  _table = 'funcionarios' # nombre de la tabla en base de datos
  _description = 'Datos de los funcionarios' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    #'cedula': columns.VarChar('cedula'),
    'cedula': columns.Integer('cedula'),
    'nombre': columns.VarChar('nombre'),
    'cargo': columns.VarChar('cargo'),
    'sueldo': columns.Integer('sueldo'), # minval=1, default=2
    'fecha_ingreso': columns.VarChar('fecha_ingreso', size=10)  # Suponiendo formato 'YYYY-MM-DD'
  }