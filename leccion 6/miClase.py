class MiClase:
    variables_clase = 'Valor variable clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    @staticmethod # solo para la variable de clase
    def metodo_estatico():
        print(MiClase.variables_clase)
        
    @classmethod
    def metodo_clase(cls):
        print(cls.variables_clase)
        
        
MiClase.metodo_clase()
miObjeto1 = MiClase('variable instancia')
miObjeto1.metodo_clase()