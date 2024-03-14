import datetime as datetime
class Implantes:

  def __init__(self, material, tamaño, medico, estado,fecha_r):
    self.__material = material
    self.__tamaño = tamaño
    self.__fecha_i = datetime.datetime.now().strftime("%d/%m/%Y")
    self.__fecha_r = fecha_r
    self.__medico = medico
    self.__revision = {} 
    self.__estado = estado
    self.__mantenimiento = ""
