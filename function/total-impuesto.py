#Ejercicio: Calculadora de Impuestos
#Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)


def Total_del_pago(pago,impuesto):
    pago_total = pago + pago *  ( impuesto / 100)
    return pago_total 


mostrar = Total_del_pago(500,6)
print(mostrar)


pago_sin_impuesto = float(input( 'Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto:'))
pago_con_impuesto = Total_del_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')