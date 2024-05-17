#formas de contatenar en python

nombre="MarleneAmi Ontiveros"
especialidad="area de Software Multiplataforma"
carrera="Ingenieria de Gestión de Desarrollo de Software"

#1er forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+" y estudio la carrera de "+carrera)

print("\n")

#2da forma
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," y estudio la carrera de ",carrera)

print("\n")


#3er forma MAS COMUN EN PYTHON
print(f"Mi nombre es ,{nombre}, estoy en la especialidad de ,{especialidad}, y estudio la carrera de ,{carrera}")

print("\n")

#4ta forma 
print("Mi nombre es ,{}, estoy en la especialidad de ,{}, y estudio la carrera de ,{}".format(nombre,especialidad,carrera))

print("\n")

#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de '+especialidad+' y estudio la carrera de '+carrera)

print("\n")
