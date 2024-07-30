# Profundizando tipo float
a = 3.0
# Constructor float puede recibir int  y str
a = float(10)
a = float('10')
# print(f'a: {a:.2f}')
# Notación exponencial (valores positivos o negativos)
x = 3e5
print(f"a: {x:.5f}")
b = 3e-5
print(f'a: {b:.5f}')
# Cualquier cálculo que involucre un float, se promueve a float
a = 4 + 5.0
print(a)
print(type(a))