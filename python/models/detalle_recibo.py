from app import models, columns
from . import funcionarios

# Recibos de Sueldo (Año/mes, TipoRecibo (sueldos, aguinaldo, vacaciones), CedulaFuncionario, NombreEmpleador, DetalleReciboId

class DetalleRecibo(models.Model):
  _table = 'detalle_recibo' # nombre de la tabla en base de datos
  _description = 'Detalles de recibos de sueldo.' # nombre del modelo en lenguaje humano

  # columnas de la tabla (la columna ID es implícita)
  _columns = {
    'detalle_recibo_id': columns.Integer('detalle_recibo_id'),  # Columna para el ID
    'tipo_concepto': columns.VarChar('tipo_concepto', allowed_values=['asignacion', 'deduccion']),
    'cantidad': columns.Integer('cantidad'),
    'monto': columns.Integer('monto')
  }
