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

class ImplanteDental(Implantes):

  def __init__(self, forma, fijacion_s, material,medico,estado):
    super().__init__(material, None, medico, estado,None)
    self.__forma = forma
    self.__fijacion_s = fijacion_s

  def verForma(self):
    return self.__forma
  def verFijacion_s(self):
    return self.__fijacion_s

  def asignarForma(self, f):
    self.__forma = f
  def asignarFijacion_s(self, f):
    self.__fijacion_s = f

class ImplanteRodilla(Implantes):

  def __init__(self, material, fijacion_t, tamaño,medico,estado):
    super().__init__(material, tamaño, medico, estado, None)
    self.__fijacion_t = fijacion_t

  def verFijacion_t(self):
    return self.__fijacion_t
    
  def asignarFijacion_t(self, f):
    self.__fijacion_t = f


class ImplanteCadera(ImplanteRodilla):

  def __init__(self, material, fijacion_t, tamaño,medico,estado):
    super().__init__(material, fijacion_t, tamaño,medico,estado)

class Paciente():
  def __init__(self, nombre, cedula):
    self.__nombre = nombre
    self.__cedula = cedula

  def verNombre(self):
    return self.__nombre
  def verCedula(self):
    return self.__cedula

  def asignarNombre(self, n):
    self.__nombre = n
  def asignarCedula(self, c):
    self.__cedula = c

class Sistema:

  def __init__(self):
    self.__inventario = {}

  def verInventario(self):
    return self.__inventario
  def verificarPaciente(self, paciente):
    if paciente in self.__inventario:
      return True
    return False 

  def ingresarPaciente(self, paciente):
    if self.verificarPaciente(paciente):
      print("El paciente ya existe")
    else:
      self.__inventario[paciente] = []

  def agregarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].append(implantes)
      print("Implante asignado al paciente correctamente\n")
    else:
      print("El paciente no existe\n")

  def eliminarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].remove(implantes)
    else:
      print("El paciente no existe\n")

  def verificarImplante(self,object,tipo):
      if isinstance(object,tipo):
        return False
      return True