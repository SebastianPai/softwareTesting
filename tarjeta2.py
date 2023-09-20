#Integrantes: 
# - Jhon Sebastian Pai
#- Jhon Brayan Muñoz
#- Jhonatan Vasquez

import re
from datetime import datetime

def validar_tarjeta(num_tarjeta, fecha_expiracion, codigo_verificacion, monto_compra):
    if len(num_tarjeta) != 16:
        return False

    try:
        fecha_expiracion = datetime.strptime(fecha_expiracion, '%m/%y')
        if fecha_expiracion <= datetime.now():
            return False
    except ValueError:
        return False
    
    if len(codigo_verificacion) != 3:
        return False
    
    if not re.match('^[0-9]+$', num_tarjeta) or not re.match('^[0-9]+$', codigo_verificacion):
        return False
    

    # Verificar si hay suficiente dinero para realizar la compra
    # Supongamos que el saldo en la tarjeta es de 1000 unidades monetarias
    saldo_tarjeta = 10000  # Cambia esto según el saldo real

    if monto_compra > saldo_tarjeta:
        return False, "Saldo insuficiente"

    return True, "Tarjeta válida y saldo suficiente"

#datos prueba


num_tarjeta = input("Ingrese el número de tarjeta de crédito: ")
fecha_expiracion = input("Ingrese la fecha de expiración (MM/YY): ")
codigo_verificacion = input("Ingrese el código de verificación: ")
monto_compra = int(input("Digite el monto de la compra: "))

# Validar la tarjeta
es_tarjeta_valida, mensaje = validar_tarjeta(num_tarjeta, fecha_expiracion, codigo_verificacion, monto_compra)

# Mostrar el resultado
print("Resultado de la validación:")
if es_tarjeta_valida:
    print("La tarjeta es válida y hay saldo suficiente.")
else:
    print("La tarjeta no es válida. Motivo:", mensaje)
