import random
from datetime import datetime
class Receta:
    def __init__(self,id,nombre,objetivo,reactivos_utilizados,procedimiento,valores_medir):
        """
        Inicializa un objeto Receta con los siguientes parametros:
        id: Id de la receta
        nombre: nombre de la receta
        objetivo: objetivo de la receta
        reactivos_utilizados: lista de reactivos utilizados y sus cantidades
        procedimiento: procedimiento para realizar la receta
        valores_medir: valores a medir en la receta
        """
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados
        self.procedimiento= procedimiento
        self.valores_medir = valores_medir

    def guardar_receta(self):            
        """
        Guarda la receta en un diccionario con sus respectivos datos.
        :return: Un diccionario con los datos de la receta
        """
        datos_experimento = {
            "id": self.id,
            "nombre": self.nombre,
            "objetivo": self.objetivo,
            "reactivos_utilizados": self.reactivos_utilizados,
            "procedimiento": self.procedimiento,
            "valores_a_medir": self.valores_medir 
        }
        return(datos_experimento)
    def mostrar(self):
        """
        Muestra la receta con todos sus datos.
        """
        datos_receta = [
            ("ID", self.id),
            ("Nombre", self.nombre),
            ("Objetivo", self.objetivo),
            ("Reactivos utilizados", self.reactivos_utilizados),
            ("Procedimiento", self.procedimiento),
            ("Valores a medir", self.valores_medir)
        ]
    
        print("Receta")
        print("-----")
        for titulo, valor in datos_receta:
            print(f"{titulo}: {valor}")
        print("-----")
    def calcular_disponibilidad(self, reactivos):
        """
        Verifica si todos los reactivos necesarios para la receta estan disponibles.
        Verifica si la cantidad necesaria de cada reactivo es menor o igual que el inventario actual
        y si la fecha de caducidad del reactivo es posterior a la fecha actual.
        :param reactivos: lista de reactivos
        :return: True si todos los reactivos estan disponibles, False de lo contrario
        """
        for x in self.reactivos_utilizados:
            for y in reactivos:
                if x["reactivo_id"] == y.id:
                    fecha = datetime.now()
                    fecha = fecha.strftime("%Y-%m-%d")
                    fecha = datetime.strptime(fecha,"%Y-%m-%d")
                    if x["cantidad_necesaria"]>y.inventario or datetime.strptime(y.fecha_caducidad,"%Y-%m-%d") < fecha  :
                        
                        return False
        return True
    def realizar(self, reactivos):
        """
        Realiza la receta utilizando los reactivos disponibles, actualiza el inventario de reactivos
        y calcula el costo total del experimento.

        Verifica primero la disponibilidad de los reactivos necesarios. Si todos los reactivos están
        disponibles, utiliza una cantidad aleatoria de cada reactivo (basado en la cantidad necesaria
        y un rango de variación) y actualiza el inventario. Calcula el costo total del uso de reactivos.

        :param reactivos: lista de objetos tipo Reactivo disponibles en el inventario.
        :return: El costo total del experimento si es realizable, de lo contrario False.
        """
        if(self.calcular_disponibilidad(reactivos)):
            
            costo = 0
            for x in self.reactivos_utilizados:
                for y in reactivos:
                    if int(x["reactivo_id"]) == y.id:
                        aux = int(x["cantidad_necesaria"]) 
                        aux2 = int(x["cantidad_necesaria"]*0.1/100)
                        aux3 =int(x["cantidad_necesaria"]*22.5/100)
                        aux += random.randint(aux2, aux3)
                        y.inventario -= aux
                        costo = costo + y.costo * aux
            
            return costo
        return False
                        
            
