class Experimento:
    def __init__(self,id, receta_id, fecha, responsables, costo, resultado):
        """
        Inicializa un objeto tipo Experimento con los parametros dados
        :param id: Identificador unico del experimento
        :param receta_id: Identificador unico de la receta utilizada
        :param fecha: fecha en que se realizo el experimento
        :param responsables: lista de las personas responsables del experimento
        :param costo: costo total del experimento
        :param resultado: resultado del experimento
        """
        self.id = id
        self.receta_id = receta_id
        self.fecha = fecha
        self.responsables = responsables
        self.costo = costo
        self.resultado = resultado



    def guardar_experimento(self):
        """
        Guarda el experimento en un diccionario con sus respectivos datos
        :return: Un diccionario con los datos del experimento
        """
        datos_experimento = {
                "id": self.id,
                "receta_id": self.receta_id,
                "personas_responsables": self.responsables,
                "fecha": self.fecha ,
                "costo_asociado": self.costo,
                "resultado": self.resultado,
                
            }
        return(datos_experimento)
    def mostrar(self):
       """
       Muestra los datos del experimento en formato de tabla.
       """
       datos_experimento = [
           ("ID", self.id),
           ("Receta ID", self.receta_id),
           ("Personas responsables", self.responsables),
           ("Fecha", self.fecha),
           ("Costo asociado", self.costo),
           ("Resultado", self.resultado)
       ]
   
       print("Datos del experimento:")
       print("------------------------")
       for titulo, valor in datos_experimento:
           print(f"{titulo}: {valor}")
       print("------------------------")

