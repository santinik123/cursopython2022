#EJERCICIO 7: CISTERNA 


cisterna = int(input("Nivel de agua: "))



if (cisterna > 6 and cisterna > 6):
    print("Desbordamiento de agua")
if (cisterna >= 6 and cisterna <= 6):
    print("Apagar bomba")
if (cisterna >= 4 and cisterna < 6):
    print("Desacelarar bomba")
elif (cisterna >= 2 and cisterna < 4):
    print("Bomba trabajando")
elif (cisterna > 0 and cisterna <= 2):   
    print("Acelerar bomba de agua")
elif (cisterna >= 0 and cisterna <= 0):
    print("Encender bomba de agua")
elif (cisterna <0 or cisterna < 0):   
    print("Fuga en cisterna")
    