# Convertido de grado celcios a faralfel


def celcios_a_fahrenheit(celcios):
    grados_fahrenheit = (celcios * 9 / 5 ) + 32
    return grados_fahrenheit




grados_fahreneheit = celcios_a_fahrenheit(5)
print(grados_fahreneheit)


# convertir de grados  faralhel a celcios

def Farahel_a_celcios(grados_farhel):
    celcios = (grados_farhel - 32 ) * 5 / 9
    return celcios


grados_celcios= Farahel_a_celcios(41)
print(grados_celcios)