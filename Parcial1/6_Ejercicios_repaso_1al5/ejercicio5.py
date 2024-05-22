#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))

if num1<num2:
   num1+=1
   for num in range (num1,num2):
       print(num)

    #mayor
else:
   print("El primer numero debe ser nemor que el segundo")  




