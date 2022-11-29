#EJERCICIO 6: CALCULAR NOMINA 

#ENTRADA DE DATOS
mes = input("ingrese mes:")
dias_laborables = input("ingrese dias laborables")
pago_por_dia = 250.00


#PROCESOS

pago_base_mensual = dias_laborables * pago_por_dia
iva_trasladado = pago_base_mensual * 0.16
subtotal = pago_base_mensual + iva_trasladado
iva_retenido = 2/3 / iva_trasladado
isr_retenido = pago_base_mensual * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido


#SALIDA DE DATOS
print("el pago base mensaul es:", pago_base_mensual)
print("el iva trasladado es:", iva_trasladado)
print("el subtotal es:", subtotal)
print("el iva retenido es:", iva_retenido)
print("el isr retenido es:", isr_retenido)
print("el subtotal es:", subtotal)


















