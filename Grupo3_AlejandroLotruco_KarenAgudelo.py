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
  
def main():
  sis = Sistema()
  while True:
    menu = int(
        input("""Escoja una opcion 
                            \r1. Ingresar Paciente
                            \r2. Modificar Informacion para un paciente
                            \rIngrese--> """))
    if menu == 1:
      nombre = input("ingrese nombre del paciente: ").lower()
      cc = int(input("ingrese la cedula del paciente: "))
      pac_new = Paciente(nombre, cc)
      sis.ingresarPaciente(pac_new)
      print(" Paciente Ingresado\n")

    elif menu == 2:
      name = input("Ingrese el nombre del paciente: ")
      doc = input("Ingrese el documento del paciente: ")
      inventario = sis.verInventario()
      for patient in sis.verInventario().keys():        
        if patient.verNombre().lower() == name.lower() and patient.verCedula() == int(doc):
            opcion = int(
                input("""Escoja una opcion 
                                        \r1. Agregar nuevos implantes 
                                        \r2. Eliminar implantes
                                        \r3. Editar informacion de implantes 
                                        \r4. Visualizar inventario completo
                                        \r5. Revision
                                        \r6. Mantenimiento
                                        \r7. Salir
                                        \rIngrese--> """))            
            if opcion == 1:
                while True:
                    print("""Protesis
                                    \r1. Marcapasos 
                                    \r2. Stend Coronario
                                    \r3. Implante Dental
                                    \r4. Implante Rodilla
                                    \r5. Implante Cadera""")
                    opcion_f = int(input("Seleccione el tipo de protesis que desea agregar: "))
                    if opcion_f == 1:                          
                        elec = input("Ingrese la cantidad de electrodos: ")
                        conec = input("Ingrese la conectividad: ")
                        frec = input("Ingrese la frecuencia: ")
                        med = input("Ingrese el medico: ")
                        est = input("Ingrese el estado: ")
                        mar = Marcapasos(elec, conec, frec,med,est)
                        sis.agregarImplantes(patient, mar)
                        subopcion = int(input("""Desea ingresar otro implante 
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break                     
                
                    elif opcion_f == 2:                                
                        mat = input("Ingrese el material: ")
                        long = input("Ingrese la longitud: ")
                        diam = input("Ingrese el diametro: ")
                        med = input("Ingrese el medico: ")
                        est = input("Ingrese el estado: ")
                        stend = StendCoronario(mat, long, diam,med,est)
                        sis.agregarImplantes(patient, stend)
                        print("Protesis agregada correctamente ")
                        sis.agregarImplantes(patient, mar)  
                        subopcion = int(input("""Desea ingresar otro implante 
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                  
                    elif opcion_f == 3:                                        
                        form = input("Ingrese la forma: ")
                        sf = input("Ingrese el sistema de fijacion: ")
                        mat = input("Ingrese el material: ")
                        med = input("Ingrese el medico: ")
                        est = input("Ingrese el estado: ")
                        im_dent = ImplanteDental(form, sf, mat,med,est)
                        sis.agregarImplantes(patient, im_dent)
                        print("Protesis agregada correctamente ")
                        subopcion = int(input("""Desea ingresar otro implante 
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                
                    elif opcion_f == 4:                                        
                        mat = input("Ingrese el material: ")
                        tf = input("Ingrese el tipo de fijacion: ")
                        tam = input("Ingrese el tamaño: ")
                        med = input("Ingrese el medico: ")
                        est = input("Ingrese el estado: ")
                        im_rod = ImplanteRodilla(mat, tf, tam,med,est)
                        sis.agregarImplantes(patient, im_rod)
                        print("Protesis agregada correctamente ")
                        subopcion = int(input("""Desea ingresar otro implante 
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                      
                    elif opcion_f == 5:                                          
                        mat = input("Ingrese el material: ")
                        tf = input("Ingrese el tipo de fijacion: ")
                        tam = input("Ingrese el tamaño: ")
                        med = input("Ingrese el medico: ")
                        est = input("Ingrese el estado: ")
                        im_cad = ImplanteCadera(mat, tf, tam,med,est)
                        sis.agregarImplantes(patient, im_cad)
                        subopcion = int(input("""Desea ingresar otro implante 
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                        
                    else:
                        print("Ingrese una opcion valida")

            elif opcion == 2:
                while True:
                    print("""Protesis
                        \r1. Marcapasos 
                        \r2. Stend Coronario
                        \r3. Implante Denal
                        \r4. Implante Rodilla
                        \r5. Implante Cadera""")
                    opcion_f = int(input("Seleccione el tipo de protesis que desea eliminar: "))
                    if opcion_f == 1:
                        for implante in inventario[patient][:]:                  
                            if isinstance(implante, Marcapasos):
                                sis.eliminarImplantes(patient, implante)
                                print("Marcapasos eliminado correctamente ")
                        subopcion = int(input("""Desea eliminar otro implante 
                                                        \r1. Si 
                                                        \r2. No 
                                                        \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                            
                            
                    elif opcion_f == 2:
                        for implante in inventario[patient][:]:
                            if isinstance(implante, StendCoronario):
                                sis.eliminarImplantes(patient, implante)
                                print("Stend coronario eliminado correctamente")
                        subopcion = int(input("""Desea eliminar otro implante 
                                                    \r1. Si 
                                                    \r2. No 
                                                    \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                    elif opcion_f == 3:
                        for implante in inventario[patient][:]:                            
                            if isinstance(implante, ImplanteDental):
                                sis.eliminarImplantes(patient, implante)
                                print("Implante dental eliminado correctamente")
                        subopcion = int(input("""Desea eliminar otro implante 
                                                    \r1. Si 
                                                    \r2. No 
                                                    \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break

                    elif opcion_f == 4:
                        for implante in inventario[patient][:]:
                            if isinstance(implante, ImplanteRodilla):
                                sis.eliminarImplantes(patient, implante)
                                print("Implante de rodilla eliminado correctamente")
                        subopcion = int(input("""Desea eliminar otro implante 
                                                    \r1. Si 
                                                    \r2. No 
                                                    \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break

                    elif opcion_f == 5:
                        for implante in inventario[patient][:]:
                            if isinstance(implante, ImplanteCadera):
                                sis.eliminarImplantes(patient, implante)
                                print("Implante de cadera eliminado correctamente")
                        subopcion = int(input("""Desea eliminar otro implante 
                                                    \r1. Si 
                                                    \r2. No 
                                                    \rIngrese su opcion: """))
                        if subopcion == 1:
                            continue
                        elif subopcion == 2 :
                            break
                    else:
                        print("Ingrese una opcion valida")
                        break

