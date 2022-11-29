#EJERCICIO 1: PROMEDIO DE 3 CALIFICACIONES 

#ENTRADAS DE DATOS

califificacion1 = float(input("escribe la primera calificacion:"))
if(califificacion1 < 0 or califificacion1 >10):
 print("promedio incorrecto")
 exit(0)

califificacion2 = float(input("escribe la segunda calificacion:"))
if(califificacion2 < 0 or califificacion2 >10):
 print("promedio incorrecto")
 exit(0)

califificacion3 = float(input("escribe la tercera calificacion:"))
if(califificacion3 < 0 or califificacion3 >10):
  print("promedio incorrecto")
  exit(0)


#PROCESOS

suma = califificacion1 + califificacion2 + califificacion3
promedio =  suma / 3

if(promedio > 6 and promedio <= 10): 
        print("Aprobado")
if(promedio >= 6 and promedio <= 6):
        print("aprobado de pansaso")
elif(promedio > 0 and promedio < 6):
        print("reprobado")
elif(promedio < 0 or promedio >10):
        print("promedio invalido")
        

        


#SALIDA DE DATOS
print("el promedio es:", promedio)
