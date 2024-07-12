#Creacion de clases

class Usuarios:
    def __init__(self, nombre, direccion, tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel


    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre=nombre

    def getDirecciion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion=direccion

    def getTelefono(self):
        return self.tel

    def setTelefono(self, tel):
        self.tel=tel

    def info_usuario(self):
        print(f"El usuario es {self.getNombre()}, su direccion es {self.getDirecciion()}, su numero de telefono es {self.getTelefono()}")

    


class Clientes(Usuarios):
    def __init__(self, nombre, direccion, tel, num_cliente ):
        super().__init__(nombre, direccion, tel )
        self.__num_cliente=num_cliente


    def getNUmcliente(self):
        return self.__num_cliente

    def setNumcliente(self, num_cliente):
        self.__num_cliente=num_cliente

        
    def info_usuario(self):
        print(f"El usuario {self.getNUmcliente()} es el cliente {self.getNUmcliente()}, su direccion es {self.getDirecciion()}, su numero de telefono es {self.getTelefono()}")


class Empleados(Usuarios):
    def __init__(self, nombre, direccion, tel, salario, num_empleado, tipo ):
        super().__init__(nombre, direccion, tel)
        self._salario=salario
        self._num_empleado=num_empleado
        self._tipo=tipo

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario=salario

    def getNumempleado(self):
        return self._num_empleado

    def setNumempleado(self, num_empleado):
        self._num_empleado=num_empleado

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo=tipo


    def info_usuario(self):
        print(f"El usuario {self.getNombre()} es el empleado {self.getNumempleado()} es de tipo {self.getTipo()}, su direccion es {self.getDirecciion()}, su numero de telefono es {self.getTelefono()}, tiene un salario de {self.getSalario()}")

