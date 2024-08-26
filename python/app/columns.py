from typing import Any
import json

def load_database():
  database = json.load(open('app\database.json'))
  for model in database:
    database[model].sort(key=lambda record: record['id'])
  return database

class Column:
  _type = None
  def __init__(self, name, default=None):
    self.name = name
    self.default = default

  def validate_value(self, value: Any):
    if value and not isinstance(value, self._type):
      raise ValueError('invalid value')

  def return_parsed_value(self, value: Any):
    return self._type(value)


# Agregue aca allowed values
class VarChar(Column):
  _type = str

  def __init__(self, name, size=None, default='', allowed_values=None):
    self.name = name
    self.size = size
    self.default = default
    self.allowed_values = allowed_values

  def validate_value(self, value: str):
    super().validate_value(value)
    if value and self.size and len(value) > self.size:
      raise ValueError('value too long')
    if self.allowed_values and value not in self.allowed_values:
            raise ValueError(f'{value} is not an allowed value')

class Integer(Column):
  _type = int

  def __init__(self, name, minval:int=None, maxval:int=None, default=0):
    self.name = name
    self.minval = minval
    self.maxval = maxval
    self.default = default

  def validate_value(self, value: str):
    super().validate_value(value)
    if value:
      if self.minval and value < self.minval:
        raise ValueError('value under minimun')
      elif self.maxval and value > self.maxval:
        raise ValueError('value over maximum')

class Decimal(Integer):
  _type = float

class Boolean(Column):
  _type = bool

  def __init__(self, name, default=False):
    self.name = name
    self.default = default

class Relation(Column):
  _type = int
  
  def __init__(self, name, relmodel, default=-1):
    self.name = name
    self.relmodel = relmodel
    self.default = default

  def return_parsed_value(self, value: Any):
    if value <= 0:
      return None
    return self.relmodel.browse(self._type(value))
