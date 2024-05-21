#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa



def main(): #punto de entrada
    while True: #Bucle infinito, se ejecutará hasta encontrar una....
        num=int(input("Introduce un número (111 si desea salir):  "))
        if num==111: #......instruccion para salir del bucle
            print("....Saliendo del programa...")
            break

if __name__ == "__main__":  #asegura quese ejecute solo si ejecutamos este archivo directamente 
    main()

