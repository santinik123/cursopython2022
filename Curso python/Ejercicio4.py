#EJERCICO 4: CALCULAR GRADOS



#ENTRADAS DE DATOS
grados = float(input("ingresa los grados:"))




#PROCESOS
c1 = grados - 273.15
c2 = 5*(grados - 32) / 9
k1 = grados + 273.15
k2 = 5*(grados-32) + 273.15 / 9
f1 = 9*(grados-273.15) + 32 / 5
f2 = 9 * grados + 32 / 5




#SALIDA DE DATOS

print("los grados celsius son:", c1)
print("los grados celsius2 son:", c2)
print("los grados kelvin son:", k1)
print("los grados kelvin2 son:", k2)
print("los grados fahrenheit son:", f1)
print("los grados fahrenheit2 son:", f2)