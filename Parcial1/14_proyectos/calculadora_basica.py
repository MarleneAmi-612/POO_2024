

import os

# Importar las funciones específicas
import otras_funciones

opcion1=True
os.system("cls") 
while opcion1:
    os.system("cls")
    print(".:: CALCULADORA BÁSICA ::. \n 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-POTENCIA\n 6.-RAIZ \n 7.-SALIR")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="7":
       n1, n2 = otras_funciones.solicitarNumeros()
       print(otras_funciones.operacionAritmetica(n1,n2, opcion))
       otras_funciones.esperarTecla()
    else:
       opcion1=False
       print("Terminaste la ejecucion del SW")




    



         

        
    
    
    




    









