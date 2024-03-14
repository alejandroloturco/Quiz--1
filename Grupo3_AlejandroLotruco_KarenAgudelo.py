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

class Marcapasos(Implantes):

  def __init__(self, electrodos, conectividad, frecuencia, medico, estado):
    super().__init__(None, None, medico, estado,None)
    self.__electrodos = electrodos
    self.__conectividad = conectividad
    self.__frecuencia = frecuencia

  def verElectrodos(self):
    return self.__electrodos
  def verConectividad(self):
    return self.__conectividad
  def verFrecuencia(self):
    return self.__frecuencia

  def asignarElectrodos(self, e):
    self.__electrodos = e
  def asignarConectividad(self, c):
    self.__conectividad = c
  def asignarFrecuencia(self, f):
    self.__frecuencia = f

class StendCoronario(Implantes):

  def __init__(self, material, longitud, diametro,medico,estado,):
    super().__init__(material,None,medico,estado,None)
    self.__longitud = longitud
    self.__diametro = diametro

  def verLongitud(self):
    return self.__longitud
  def verDiametro(self):
    return self.__diametro

  def asignarLongitud(self, l):
    self.__longitud = l
  def asignarDiametro(self, d):
    self.__diametro = d
