from veterinaria import *

# Crear el objeto cliente1
cliente1 = Clientes(
    identificador=4598478,
    nombre="Juan Chuchin",
    edad=23,
    telefono="618123948",
    correo="juan@gmail.com"
)

# Crear el objeto animal1
animal1 = Animales(
    nombre="Piolin",
    edad=3,
    especie="pajaro",
    raza="desconocida",
    color="amarillo",
    tamaño="pequeño",
    esterilizado=False,
    vacunas=False
)

# Crear el objeto empleado1
empleado1 = Empleados(
    identificador=1,
    nombre="Mariela Vazquez",
    edad=45,
    telefono="61898034",
    correo="mariela@agencia.com",
    titulo="Doctor cirujano",
    especialidad="esterilizaciones",
    encargado_servicio="Cirugías"
)

# Verificar los datos de los objetos
print(f"Cliente: {cliente1.getNombre()}, Edad: {cliente1.getEdad()}, Teléfono: {cliente1.getTelefono()}, Correo: {cliente1.getCorreo()}, ID: {cliente1.getIdentificador()}")
print(f"Animal: {animal1.getNombreMascota()}, Edad: {animal1.getEdadMasc()}, Especie: {animal1.getEspecie()}, Raza: {animal1.getRaza()}, Color: {animal1.getColor()}, Tamaño: {animal1.getTamaño()}, Esterilizado: {animal1.getEsterilizado()}, Vacunas: {animal1.getVacunas()}")
print(f"Empleado: {empleado1.getNombre()}, Edad: {empleado1.getEdad()}, Teléfono: {empleado1.getTelefono()}, Correo: {empleado1.getCorreo()}, Título: {empleado1.getTitulo()}, Especialidad: {empleado1.getEspecialidad()}, Servicio: {empleado1.getEncargadoServicio()}")
