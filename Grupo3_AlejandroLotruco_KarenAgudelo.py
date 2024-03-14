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

  def verMaterial(self):
    return self.__material
  def verTamaño(self):
    return self.__tamaño
  def verMedico(self):
    return self.__medico
  def verEstado(self):
    return self.__estado
  def verRevision(self):
    return self.__revision
  def fecha_r(self):
    return self.__fecha_r
  def fecha_i(self):
    return self.__fecha_i
  def verMantenimiento(self):
    return self.__mantenimiento

  def asignarMaterial(self, m):
    self.__material = m
  def asignarTamaño(self, t):
    self.__tamaño = t
  def asignarMedico(self, med):
    self.__tamaño = med
  def asignarEstado(self, e):
    self.__tamaño = e
  def asignarFecha_r(self, r):
    self.__fecha_r = r
  def asignarRevision(self,sis2 ,fecha, manten):
    if fecha in sis2:
      self.__revision[fecha].append(manten)     
    else:
      self.__revision[fecha] = []
      self.__revision[fecha].append(manten)
    print("mantenimiento registrado exitosamente\n")

  def asignarMantenimiento(self,m):
    self.__mantenimiento = m
