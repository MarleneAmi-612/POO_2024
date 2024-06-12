# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

frutas=["mangos", "platanos", "sandias"]
frase="Sentado debajo de un arbol, sentado en un arbol de mangos "
num=100
comer=True

def mensajote(variable):
    if isinstance(variable, list):  #isinstance determina el valor de la variable 
        print(f"{variable} Esta es una lista.")
    elif isinstance(variable, str):
        print(f"{variable} Esta es una cadena.")
    elif isinstance(variable, int):
        print(f"{variable} Este es un entero.")
    elif isinstance(variable, bool):
        print(f"{variable} Este es un valor lógico.")
    else:
        print("Tipo de dato desconocido.")


mensajote(frutas)
mensajote(frase)
mensajote(num)
mensajote(comer)


#NUEVO
#                    """"""""isinstance"""""""""""""
#verificar si un objeto es una instancia de una clase o tipo de dato específico. 
#La sintaxis de isinstance es la siguiente:
#          isinstance(objeto, clase_o_tipo)




