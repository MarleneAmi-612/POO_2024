#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

num1=int(input("Ingrese el primer numero : "))
num2=int(input("Ingrese el segundo numero :"))

#Cálculos
sume=num1+num2
reste=num1-num2
divi=num1/num2
multiple=num1*num2

print(f"RESULTADO SUMA: {sume}")
print(f"RESULTADO RESTA: {reste}")
print(f"RESULTADO DIVISIÓN: {divi}")
print(f"RESULTADO MULTIPLICACION: {multiple}")
