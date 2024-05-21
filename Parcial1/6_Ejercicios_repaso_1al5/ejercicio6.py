#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

i=1

while i<=10:
    print("")
    print(f"TABLA DEL {i}")
    for num in range(1,11):
        multi=i*num
        print(f"{i} x {num} = {multi}")
    i+=1   


        



