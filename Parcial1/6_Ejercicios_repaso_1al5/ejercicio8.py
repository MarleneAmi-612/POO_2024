#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

porc=int(input("Ingrece el porcentaje: "))
num=int(input("Ingrese el numero: "))

print(f"¿Cuanto es el {porc} por ciento de {num}?")
porcen=porc/100
numf=num*porcen
print(numf)