#Integrantes: 
#- Jhon Sebastian Pai
#- Jhon Brayan Muñoz
#- Jhonatan Vasquez
#- Kedin Benavides

import re
from datetime import datetime

def validar_tarjeta(num_tarjeta):
    if len(num_tarjeta) != 16:
        return False
    return True


def validar_fecha(fecha_expiracion):
    try:
        fecha_expiracion = datetime.strptime(fecha_expiracion, '%m/%y')
        if fecha_expiracion <= datetime.now():
            return False
    except ValueError:
        return False
    return True


def validar_codigo(codigo_verificacion):
    if len(codigo_verificacion) != 3:
        return False
    return True

  
def validar_saldo(monto_compra):
    saldo_tarjeta = 10000
    if monto_compra > saldo_tarjeta:
        return False
    return True