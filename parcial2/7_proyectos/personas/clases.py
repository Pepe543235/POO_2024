
class Personas:

    def __init__(self,nombre,edad,tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel

    def info_persona(self):
        print(f"El nombre de la persona es: {self.getNombre()}, su edad es: {self.getEdad()}, y su telefono es: {self.getTel()}") 

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getEdad(self):
        return self.edad

    def setEdad(self,edad):
        self.edad=edad

    def getTel(self):
        return self.tel

    def setTel(self,tel):
        self.tel=tel

class Estudiantes(Personas):
    def __init__(self,nombre,edad,tel,carrera,matricula):
        super().__init__(nombre,edad,tel) 
        self.__carrera=carrera
        self.__matricula=matricula

    def info_persona(self):
        print(f"El nombre de la persona es: {self.getNombre()}, su edad es: {self.getEdad()}, su telefono es: {self.getTel()}, su carrera es: {self.getCarrera()} y su matricula es: {self.getMatricula}") 

    def informar_carrera(self):
        print(f"El estudiante {self.getNombre} esta en la carrera {self.getCarrera}")

    def getCarrera(self):
        return self.__carrera

    def setNum_Cliente(self,carrera):
        self.__carrera=carrera 
    
    def getMatricula(self):
        return self.__matricula

    def setNum_Cliente(self,matricula):
        self.__matricula=matricula 

class Docentes(Personas):
    def __init__(self,nombre,edad,tel,modalidad,num_empleado):
        super().__init__(nombre,edad,tel) 
        self._modalidad=modalidad
        self._num_empleado=num_empleado

    def info_persona(self):
        print(f"El nombre de la persona es: {self.getNombre()}, su edad es: {self.getEdad()}, su telefono es: {self.getTel()}, su modalidad es: {self.getModalidad()} y su numero de empleado es: {self.getNum_Empleado}") 

    def informar_modalidad(self):
        print(f"El docente {self.getNombre} esta en la modalidad {self.getModalidad}")
    
    def getModalidad(self):
        return self._modalidad

    def setModalidad(self,modalidad):
        self._modalidad=modalidad 

    def getNum_Empleado(self):
        return self._num_empleado

    def setNum_Empleado(self,num_empleado):
        self._num_empleado=num_empleado 