#Convertir tipos de datos

#NOTA: solo es posible en una contatenacion contatenar entre tipos de datos iguales


texto="soy una cadena"
numero=23

print(texto+"Soy una cadena2")
print(numero+34)


#Convertir un tipo de dato int a str
numero_str=str(numero)
print(texto+numero_str)

print(texto+""+str(numero))

#unir a una cadena algo que no es de tipo cadena
#en este caso "texto" se une con "numero" 
#se tiene que convertir un resultado numerico en una cadena
#haciendo lo mismo que en la lines 17 MÁS COMUN


#convertir un STR A INT
n1=33
suma=int('23')+n1
print("suma: "+str(suma))

#CONVERTIR UN float A int
n1=33
n2=float(33.10)

suma=n1+n2
print(suma)


#CONVERTIR DE int A float
n1=3
n2=4

suma=n1+n2
print(f"La suma es: {suma}")