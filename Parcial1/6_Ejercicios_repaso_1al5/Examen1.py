#sueldo del trabajador

sueldo_todos=0
trabajador=0

while True:
    trabajador+=1
    nombre=str(input(f"Ingrese el nombre del trabajador {trabajador}: "))
    horas_tr=int(input("Ingrese las horas trabajadas: "))
    dias_tr=int(input("Ingrese los dias trabajados: "))
    sueldo_hora=float(input("Ingrese el sueldo que gana por hora: "))

    
    
    #calculos
    #SEMANA
    sueldo_dia=sueldo_hora*horas_tr
    sueldo_semana=sueldo_dia*dias_tr
    #MES
    mes_sueldo=sueldo_semana*4
  
    #Imprime sueldo y tipo de obrero
    print(f"Sueldo mensual: {mes_sueldo}")
    print(f"Sueldo semanal: {sueldo_semana}")

    if mes_sueldo<=10000:
           print("Obrero tipo A")
    if mes_sueldo>10000 and mes_sueldo>=15000:
               print("Obrero tipo B")

    else:
         print("Sincategoria")

    #acumula sueldo de cada uno
    sueldo_todos+=mes_sueldo
    respuesta=str(input("¿Desea otra captura? (SI/NO):  "))
    if respuesta=="NO":
        break
    


#Imprime sueldo total al terminar
print(f"El sueldo total de los {trabajador} trabajadores es de:  {sueldo_todos}")




