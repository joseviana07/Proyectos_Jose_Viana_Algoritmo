class Reactivo:
    def __init__(self,id,nombre, descripcion, costo, categoria, inventario, unidad_medicion,fecha_caducidad,minimo_sugerido,conversiones_posibles):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.categoria = categoria
        self.inventario = inventario
        self.unidad_medicion = unidad_medicion
        self.fecha_caducidad = fecha_caducidad
        self.mininimo_sugerido = minimo_sugerido
        self.conversiones_posibles = conversiones_posibles
       


    def mostrar(self):
        """
        Muestra la información del reactivo
        """
        print("*************************************")
        print("*Información del Reactivo *")
        print("*************************************")
        print(f"ID: {self.id}")
        print("-------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Costo: {self.costo}")
        print(f"Categoría: {self.categoria}")
        print(f"Inventario: {self.inventario}")
        print(f"Unidad de Medición: {self.unidad_medicion}")
        print(f"Fecha de Caducidad: {self.fecha_caducidad}")
        
    def guardar_reactivo(self):     
        """
        Guarda la informacion del reactivo en un formato JSON.
        """
        datos_experimento = {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "costo": self.costo,
            "categoria": self.categoria,
            "inventario_disponible": self.inventario,
            "unidad_medida": self.unidad_medicion,
            "fecha_caducidad": self.fecha_caducidad,
            "minimo_sugerido": self.mininimo_sugerido,
            "conversiones_posibles" : self.conversiones_posibles
        }
        return(datos_experimento)