#AHI VIENEN LAS CLASESOTAS 

class Veterinarias:
    def __init__(self, sucursal, direccion, institucion, nombre_director):
        self.sucursal = sucursal
        self.direccion = direccion
        self.institucion = institucion
        self.nombre_director = nombre_director

    def agregarEmpleado(self):
        print("El empleado ha sido agregado")

    def getSucursal(self):
        return self.sucursal

    def setSucursal(self, sucursal):
        self.sucursal = sucursal

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getInstitucion(self):
        return self.institucion

    def setInstitucion(self, institucion):
        self.institucion = institucion

    def getNombreDirector(self):
        return self.nombre_director

    def setNombreDirector(self, nombre_director):
        self.nombre_director = nombre_director


class Personas:
    def __init__(self, identificador, nombre, edad, telefono, correo):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

    def getIdentificador(self):
        return self.identificador

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo


class Animales:
    def __init__(self, nombre, edad, especie, raza, color, tamaño, esterilizado, vacunas):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.raza = raza
        self.color = color
        self.tamaño = tamaño
        self.esterilizado = esterilizado
        self.vacunas = vacunas

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def hacerNecesidades(self):
        print(f"{self.nombre} está haciendo sus necesidades.")

    def getNombreMascota(self):
        return self.nombre

    def setNombreMascota(self, nombre):
        self.nombre = nombre

    def getEdadMasc(self):
        return self.edad

    def setEdadMasc(self, edad):
        self.edad = edad

    def getEspecie(self):
        return self.especie

    def setEspecie(self, especie):
        self.especie = especie

    def getRaza(self):
        return self.raza

    def setRaza(self, raza):
        self.raza = raza

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getTamaño(self):
        return self.tamaño

    def setTamaño(self, tamaño):
        self.tamaño = tamaño

    def getEsterilizado(self):
        return self.esterilizado

    def setEsterilizado(self, esterilizado):
        self.esterilizado = esterilizado

    def getVacunas(self):
        return self.vacunas

    def setVacunas(self, vacunas):
        self.vacunas = vacunas


class Clientes(Personas):
    def __init__(self, identificador, nombre, edad, telefono, correo):
        super().__init__(identificador, nombre, edad, telefono, correo)

    def solicitar_cita(self):
        print(f"{self.nombre} ha solicitado una cita.")

    def datos_mascota(self):
        print(f"{self.nombre} está proporcionando datos de su mascota.")


class Empleados(Personas):
    def __init__(self, identificador, nombre, edad, telefono, correo, titulo, especialidad, encargado_servicio):
        super().__init__(identificador, nombre, edad, telefono, correo)
        self.titulo = titulo
        self.especialidad = especialidad
        self.encargado_servicio = encargado_servicio

    def revision_medica(self):
        print(f"{self.nombre} está realizando una revisión médica.")

    def agregar_tratamiento(self):
        print(f"{self.nombre} está agregando un tratamiento.")

    def agendarCita(self):
        print(f"{self.nombre} está agendando una cita.")

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getEspecialidad(self):
        return self.especialidad

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def getEncargadoServicio(self):
        return self.encargado_servicio

    def setEncargadoServicio(self, encargado_servicio):
        self.encargado_servicio = encargado_servicio


class Citas:
    def __init__(self, id_cita, nombre_cliente, nombre_mascota, servicio, fecha, medico):
        self.id_cita = id_cita
        self.nombre_cliente = nombre_cliente
        self.nombre_mascota = nombre_mascota
        self.servicio = servicio
        self.fecha = fecha
        self.medico = medico

    def registrarCliente(self):
        print(f"Cliente {self.nombre_cliente} registrado para la cita {self.id_cita}.")

    def getIdCita(self):
        return self.id_cita

    def setIdCita(self, id_cita):
        self.id_cita = id_cita

    def getNombreCliente(self):
        return self.nombre_cliente

    def setNombreCliente(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente

    def getNombreMascota(self):
        return self.nombre_mascota

    def setNombreMascota(self, nombre_mascota):
        self.nombre_mascota = nombre_mascota

    def getServicio(self):
        return self.servicio

    def setServicio(self, servicio):
        self.servicio = servicio

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getMedico(self):
        return self.medico

    def setMedico(self, medico):
        self.medico = medico


class Servicios:
    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio

    def limpieza(self):
        print("Realizando servicio de limpieza.")

    def diagnostico(self):
        print("Realizando servicio de diagnóstico.")

    def atencion_medica(self):
        print("Realizando servicio de atención médica.")

    def cirujias(self):
        print("Realizando servicio de cirugías.")

    def vacunacion(self):
        print("Realizando servicio de vacunación.")

    def spa(self):
        print("Realizando servicio de spa.")

    def getNombreServicio(self):
        return self.nombre_servicio

    def setNombreServicio(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio
