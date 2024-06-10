# opcion1=True
# while opcion1:
#     print("\n\t::::::::CALCULAORA BÁSICA:::::::\n 1) SUMA \n 2) RESTA \n 3) MULTIPLICACION \n 4) DIVISIÓN \n 5) SALIR ")
#     opcion=input("\t Elige una Opcion: ").upper()
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#         n1=int(input("Numero #1: "))
#         n2=int(input("Numero #2: "))
#         print(f"{n1} + {n2} = {n1+n2}")
    

#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#         n1=int(input("Numero #1: "))
#         n2=int(input("Numero #2: "))
#         print(f"{n1} - {n2} = {n1-n2}")

#     elif opcion=="3" or opcion=="/" or opcion=="DIVISION":
#         n1=int(input("Numero #1: "))
#         n2=int(input("Numero #2: "))
#         print(f"{n1} / {n2} = {n1/n2}")

#     elif opcion=="4" or opcion=="x" or opcion=="MULTIPLICACION":
#         n1=int(input("Numero #1: "))
#         n2=int(input("Numero #2: "))
#         print(f"{n1} x {n2} = {n1*n2}")

#     elif opcion=="5":
#         print("TERMINASTE LA EJECUCION EL PROGRAMA")
#         opcion1=False
    
#...........................................................
# def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Número #1: "))
#     n2=int(input("Número #2: "))

# def operacionAritmetica(num1,num2, opcion):
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#         return(f"{n1}+{n2}={n1+n2}")
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#         return(f"{n1}-{n2}={n1-n2}")
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#         return(f"{n1}X{n2}={n1*n2}")
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#         return(f"{n1}/{n2}={n1/n2}")

# def esperarTecla():
#     print("Presione una tecla para continuar....")
#     mscrt.getch() #Va a esperar a que oprima una tecla
#..................................................................


import os

# Importar las funciones específicas
import otras_funciones

opcion1=True
os.system("cls") 
while opcion1:
    os.system("cls")
    print(".:: CALCULADORA BÁSICA ::. \n 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-SALIR")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="5":
       n1, n2 = otras_funciones.solicitarNumeros()
       print(otras_funciones.operacionAritmetica(n1,n2, opcion))
       otras_funciones.esperarTecla()
    else:
       opcion1=False
       print("Terminaste la ejecucion del SW")




    



         

        
    
    
    




    









