# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


#CON FOR
for num in range(1,61):
    cuad=num*num
    print(cuad)

#CON WHILE

num=1

while num<=60:
    cuad=num*num
    print(cuad)
    num+=1
   
  