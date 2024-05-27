#Calcular el IMC 

contador=0

while True:
    peso=float(input("Ingrese su peso(kg): "))
    altura=float(input("Ingrese su altura (m): "))

    #CALCULOS
    imcc=peso/(altura*altura)
    contador+=1

    salir=str(input("¿Desea hacer otro calculo? (SI/NO)"))
    if salir=="NO":
        break


    #SALIDA
if imcc<18.5:
    print("Peso inferior al normal")
if imcc>=18.5 and imcc<=24.9:
    print("Normal")
if imcc>=25 and imcc>=29.9:
    print("Peso superior al normal")
if imcc>30:
   print("Obesidad")
    
print(f"Se hicieron {contador} cálculos ")