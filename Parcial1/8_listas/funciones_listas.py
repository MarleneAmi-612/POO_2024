paises["Mexico", "USA", "Brasil", "Japon"]
numeros[23, 100, 3.1416, 0.100]
varios["Hola", True, 100, 10.22]

#Ordenar la lista
#SOLO FUNCIONA SI TIENE SOLO STR O NUMEROS
print(paises)
paises.sort() #ordenaaaas con SORT
print(paises)

print(nnumeros)
numeros.sort()
print(nuemros)
#..............................................
#Como agegar elementos
print(numeros)
numeros.insert(len(numeros), 100) #duda con la coma

#OTRA FUNCION
print(numeros)
numeros.append(100)
print(numeros)

#.................................
#ELIMINAR EN LISTA
print(numeros)
numeros.pop(2) #eliminas la que esta en esa posicion
#Es mejor que busque donde esta y eso

#OTRO MODO
print(numeros)
numeros.remove(100) #Remove el 100 de la lista

#...............................
#BUSCAR EN LA LISTA

encontrar="Brasil" in paises #EVITAS EL FOOOR
print(numeros)


#.........................
#DAR LA VUELTA A LA LISTA
print(varios)
varios.reverse()
print(varios)

#......................
#CONTATENAR LISTAAA (UNIIIIR)
print(paises)
paises.extend(numeros)
print(paises) #Las dos listas STR y NUM se unieroooon waaaa

#.................
#VACIAR LA LISTAAAAA
print(varios)
varios.clear()
print(varios)

#...........................
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#¿QUE TECLA PRESIONE?
import msvcrt

# Espera a que el usuario presione una tecla y la almacena en la variable "tecla"
tecla = msvcrt.getch()

# Imprime la tecla presionada por el usuario
print("Presionaste la tecla:", tecla)