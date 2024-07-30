# Profundizando en el tipo str

# caracteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'  #elimina el punto
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\\juan'  #es parte de nuestra cadena
print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de línea'  #/n salto de linea
print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
print(f'Resultado: {resultado}')
