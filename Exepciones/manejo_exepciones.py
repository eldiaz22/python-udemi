from igual import Numero_identico
resultado = None
try:
    a = int(input("Ingrese su numero"))
    b = int(input("Ingrese su otro numero"))
    if a == b:
        raise Numero_identico("NUMERO IGUALES") #arror exepciones en cualquier parte de nuestro codigo
    resultado = a / b
except ZeroDivisionError as e:
    print(f" zero division You can't divide by zero! {e}, {type(e)}")
except TypeError as e:
    print(f" typeerror You can't divide by zero! {e}, {type(e)}")
except Exception as e:
    print(f"  exeption You can't divide by zero! {e} {type(e)}")
    
else: print("No ocurrio ningun error")
finally: 
    print("Siempre se ejecuta")
    
    
    
    
    
    
    
    
    
    
print(f" resultado {resultado}")
print("continuamos")