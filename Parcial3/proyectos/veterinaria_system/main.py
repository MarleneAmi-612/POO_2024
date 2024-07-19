#AQUI ESTA EL MENU DE OPCIONES
#Todo esta mal, de apoco le hacemos sus modificaciones correspondientes
#Estoy usando el menu de otro proyecto para adaptarlo en una veterinaria

from veterinaria import *
import getpass   #solicitar contraseñas al usuario sin mostrarlas en la pantalla
from funciones import *

def menu_inicial():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registrar cliente
          2.- Citas
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ")
            apellidos = input("\t ¿Cuáles son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            usuario_actual = usuario.Usuarios(None, nombre, apellidos, email, password, None)
            usuario_actual.registrar()
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            usuario_actual = usuario.Usuarios(None, None, None, email, password, None)
            if usuario_actual.iniciar_sesion(email, password):
                menu_notas(usuario_actual.id, usuario_actual.nombre, usuario_actual.apellidos)
            else:
                print("\n\tCredenciales incorrectas. Inténtalo de nuevo.")
            esperarTecla()
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\tTitulo: ")
            descripcion = input("\tDescripción: ")
            nueva_nota = nota.Notas(None, usuario_id, titulo, descripcion, None)
            nueva_nota.crear()
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            nota.Notas.mostrar(usuario_id)
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            nota.Notas.actualizar(id, titulo, descripcion)
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar una Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            # Aquí agregarías la lógica para eliminar la nota
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
