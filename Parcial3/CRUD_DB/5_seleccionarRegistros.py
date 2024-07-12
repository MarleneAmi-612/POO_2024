from conexionBD import *

try:
  micursor=conexion.cursor()

  sql="select nombre,direccion,tel from clientes"
  micursor.execute(sql)
  resultado=micursor.fetchall() #l que tienes ahi damelo todo en una lista

  if len(resultado)>0:
      print(f"Registros de la tabla: {len(resultado)}")
      for x in resultado:
        print(x)


except:
     print(f"Ocurrio un problema con el servidor... por favor intentalo mas tarde")

else:
   
    print(f"Registro Seleccionado Correctamente")
