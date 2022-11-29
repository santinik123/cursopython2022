#EJERCICIO 2: CALCULAR EL AREA Y PERIMETRO DE UN CIRUCLO

#ENTRADAS DE DATOS
radio = float(input("ingresa valor de radio:"))


#DECLARAR UNA CONSTANTE 
PI = 3.1416



#PROCESOS
area = PI * pow(radio, 2)
perimetro = 2 * PI * radio

#SALIDA DE DATOS
print("El area es:", area)
print("el perimetro es:", perimetro)
