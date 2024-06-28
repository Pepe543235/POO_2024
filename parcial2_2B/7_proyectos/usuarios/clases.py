
class Usuarios:

    def __init__(self,nombre,direccion,tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel

    def info_usuario(self):
        print(f"El nombre del usuario es: {self.getNombre()}, su direccion es: {self.getDireccion()}, y su telefono es: {self.getTel()}") 

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getDireccion(self):
        return self.direccion

    def setDireccion(self,direccion):
        self.direccion=direccion

    def getTel(self):
        return self.tel

    def setTel(self,tel):
        self.tel=tel

class Clientes(Usuarios):
    def __init__(self,nombre,direccion,tel,num_cliente):
        super().__init__(nombre,direccion,tel) 
        __self.num_cliente=num_cliente

    def info_usuario(self):
        print(f"Numero del cliente: {self.getNum_cliente()} / El nombre del cliente es: {self.getNombre()}, su direccion es: {self.getDireccion()}, y su telefono es: {self.getTel()}") 

    def getNum_Cliente(self):
        return self.__num_cliente

    def setNum_Cliente(self,num_cliente):
        self.__num_cliente=num_cliente 

class Empleados(Usuarios):
    def __init__(self,nombre,direccion,tel,salario,num_empleado,tipo):
        super().__init__(nombre,direccion,tel) 
        _self.salario=salario
        _self.num_empleado=num_empleado
        _self.tipo=tipo

    def info_usuario(self):
        print(f"Numero del empleado: {self.getNum_Empleado()} / El nombre del empleado es: {self.getNombre()}, su direccion es: {self.getDireccion()}, su salario es: {self.getSalario()}, su tipo es: {self.getTipo()}") 

    def getSalario(self):
        return self._salario

    def setSalario(self,salario):
        self._salario=salario 

    def getNum_Empleado(self):
        return self._num_empleado

    def setNum_Empleado(self,num_empleado):
        self._num_empleado=num_empleado 

    def getTipo(self):
        return self._tipo

    def setTipo(self,tipo):
        self._tipo=tipo 