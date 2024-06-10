# List (Array)
# son colecciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valores de hace con un indice numerico

#Nota: Sus valores si son modificables 

#La lista es una coleccion ordenada y modificable 
#Permite miembros


#EJEMPLO 1: Crear una lista de numeros e imprimir el contenido

# numeros=[23,34]
# # print(numeros)

# #Recorrer el contenido de una lista mediante for
# # for i in numeros:
# #     print(i)

# #Recorrer el contenico mediante while

# i=0
# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1


#EJEMPLO 2: Crear una lista de palabras y posteriormente bucar la coincidencia de una palabra 

# mylist=["hola", "HOLA", "Piolines", "PIOLINES"]

# palabra_buscar=input("Ingresa la palabra a buscar")


# if palabra_buscar in mylist:
#     for i, p in enumerate(mylist):
#         if p==palabra_buscar:
 
#            print(f"Se eccontro la palabra a buscar en la posición  {i}")
# else:
#     print("No se encontró la palabra en la lista")

#CON UN WHILE
# mylist=["hola", "HOLA", "Piolines", "PIOLINES", "PIOLINES"]
# print(mylist)

# palabra_buscar=input("Ingresa la palabra a buscar")

# encontro=False
# i=0
# while i<=len(mylist)-1:
#     if mylist[i]==palabra_buscar:
#         print(f"Se eccontro la palabra a buscar en la posición  {i}")
#         encontro=True
#     i+=1

    
# if not encontro:
#     print("No se encontró la palabra en la lista")
    

# #Ejemplo 3 Agregar y eliminar elementos de una lista
# #o.s aystem("clear")

# nuemros=[23,34,23]
# print(numeros)

# #agregar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numero)

# #eliminar un elemento
# numeros.remove(100) #Indicar el elemento a borrar
# print(numeros)
# numeros.pop(2) #Indicar la posicion del elemento a borrar
# print(numeros)

#Crear una lsta multilinea (matriz) para agregar los nombres y numeros telefonicos

# agenda=[
#     ["Carlos", 61889393],
#     ["Leo", 618766357],
#     ["Leo", 618990903],
#     ["Sebastian", 61893833],
#     ["Pedro", 9283892],
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.- {i}")


#...........................................................................................................

#EJEMPLO 5
#Crear un programa que permita Gestionar (Administrar) peliculas
#Colocar un menu de opciones para agregar, remover, consultar peliculas
#Notas
#1-. utiliar funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombress de peliculas

import os
import peliculas_funciones


gestion=True
while gestion:
    os.system("cls")
    print("\t\n....::::GESTIÓN DE PELICULAS::::.....\n 1.- AGREGAR\n 2.- REMOVER\n 3.- CONSULTAR\n 4.- BUSCAR\n 5.- SALIR")
    opcion=input("\t Elige una opcion: ").upper()

    if opcion=="1":
        os.system("cls")
        peliculas_funciones.AgregarPeli()

    elif opcion=="2":
        os.system("cls")
        peliculas_funciones.RemovePeli()

    elif opcion=="3":
        os.system("cls")
        peliculas_funciones.ConsultarPeli()

    elif opcion=="4":
        os.system("cls")
        peliculas_funciones.BuscarPeli()

    elif opcion=="5":
        os.system("cls")
        gestion=False
        print("Terminaste la ejecucion del SW")


    




    



