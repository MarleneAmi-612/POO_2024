
peliculas=["rango", "sherk", "sing"]

import msvcrt
def AgregarPeli():
    movie=input("\t¡AGREGA UNA PELICULA NUEVA! \nIngrese el nombre de la pelicula: ")
    peliculas.append(movie)
    print(f"¡Ha sido agregada {movie} con exito!")
    print("Presione una tecla para continuar......")
    msvcrt.getch()


def RemovePeli():
    print("\t¡ELIMINA UNA PELICULA!")
    print(peliculas)
    movie=input("Ingrese el nombre de la pelicula que desea remover: ")
    i=0
    encontro=False
    while i <= len(peliculas):
       
        if movie in peliculas:
             resp=input(f"Pelicula existente \n ¿Seguro de eliminar {movie}?").upper()
             if resp=="SI":
                 peliculas.remove(movie)
                 print(f"¡La pelicula {movie} ha sido removida con exito!")
                 encontro=True
        i+=1
                
    if not encontro:
         print(f"{movie} no fue encontrado en nuestra lista")

    print("Presione una tecla para continuar......")
    msvcrt.getch()

def ConsultarPeli():
    print("\t¡CONSULTA LA CARTELERA ACTUALIZADA!")
    print(peliculas)
    print("Presione una tecla para continuar......")
    msvcrt.getch()


def BuscarPeli():
    print("\t¡BUSCA UNA PELICULA!")
    movie=input("Ingresa la pelicula a buscar: ")
    
    if movie in peliculas:
        for i, p in enumerate(peliculas):
            if p==movie:
                print(f"La pelicula se encuentra en la posicion {i} de la lista")
        
    else:
        print("No se encontró la pelicula en la lista")

    print("Presione una tecla para continuar......")
    msvcrt.getch()

def VaciarPeli():
    print("\t¡VACIA TODO!")
    peliculas.clear()
    print("Presione una tecla para continuar......")
    msvcrt.getch()

