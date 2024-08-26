from app import models, columns
from . import funcionarios
from . import detalle_recibo

# Recibos de Sueldo (Anio/mes, TipoRecibo (sueldos, aguinaldo, vacaciones), CedulaFuncionario, NombreEmpleador, DetalleReciboId

class RecibosSueldo(models.Model):
  _table = 'recibos_sueldo' # nombre de la tabla en base de datos
  _description = 'Recibos de sueldo.' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implicita)
  _columns = {
    'anio_mes': columns.VarChar('anio_mes', size=7),  # Ejemplo de formato 'YYYY-MM'
    'tipo_recibo': columns.VarChar('tipo_recibo', allowed_values=['vacaciones', 'aguinaldo', 'licencia']),
    'id_funcionario': columns.Relation('id', funcionarios.Funcionarios), 
    'nombre_empleador': columns.VarChar('nombre_empleador'),
    'detalle_recibo_id': columns.Relation('detalle_recibo_id', detalle_recibo.DetalleRecibo)
  }
