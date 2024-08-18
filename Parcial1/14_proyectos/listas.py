

import os
import peliculas_funciones


gestion=True
while gestion:
    os.system("cls")
    print("\t\n....::::GESTIÓN DE PELICULAS::::.....\n 1.- AGREGAR\n 2.- REMOVER\n 3.- CONSULTAR\n 4.- BUSCAR\n 5.- VACIAR \n 6.- SALIR")
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
        peliculas_funciones.VaciarPeli()

    elif opcion=="6":
        os.system("cls")
        gestion=False
        print("Terminaste la ejecucion del SW")


    




    



