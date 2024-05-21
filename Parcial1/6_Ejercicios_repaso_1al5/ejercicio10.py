#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron


reprobad=0
aprobad=0
for contador in range(1,16):

     calif=float(input(f"Ingrese la calificación del alumno {contador} (ej. 100): "))
     
     if calif<=79:
        reprobad+=1
     if calif>=80:
        aprobad+=1

print(f"{aprobad} aprobados en total")
print(f"{reprobad} reprobados en total") 

