from funciones import *  
import requests
import json
from reactivo import Reactivo as reac
from experimento import Experimento as ex
from receta import Receta  as rec
from reactivo_utilizado import ReactivoUtilizado
from valores import Valores_medir
class App:
    def __init__(self):
        """
        Inicializa el objeto App, creando las listas que se necesitan para guardar los datos de los reactivos, experimentos, recetas, reactivos utilizados y valores a medir.
        """
        self.reactivos = []
        self.experimentos = []
        self.recetas = []
        self.reactivo_utilizado = []
        self.valores_medir = []
    


    def menu_principal(self):
        """
        Menu principal del programa, se encarga de mostrar las opciones principales del programa y
        redirigir a los diferentes menus segun la opcion seleccionada.

        Primero intenta cargar los datos desde un archivo, si no puede cargarlos intenta obtenerlos desde
        la api y si no puede obtenerlos desde la api, levanta una excepcion.

        Luego entra en un bucle infinito en el que se encarga de mostrar las opciones y redirigir a los
        diferentes menus segun la opcion seleccionada, hasta que el usuario decida salir del programa

        :return: None
        """
        try:
            self.carga_normal()
        except:
            self.carga_inicial()
        while True:
            opcion = input("Seleccione una opcion:\n1-Reactivos\n2-Experimentos\n3-Estadisticas\n4-Recargar Datos De la api\n5-Salir\n--->")  
            if opcion == "1":
                self.menu_reactivo()
            elif opcion == "2":
                self.menu_experimento()
            elif opcion == "3":
                self.estadisticas()    
            elif opcion == "4":
                self.carga_inicial()
            elif opcion == "5":
                self.guardar()
                break
            else:
                print("Introduzca solo uno de los valores señalados")
    def menu_reactivo(self):
        """
        Menu que se encarga de mostrar las opciones relacionadas con los reactivos,
        se encarga de redirigir a los diferentes menus segun la opcion seleccionada.

        Muestra las opciones para mostrar los reactivos, agregar un reactivo, eliminar un reactivo, editar un reactivo,
        o salir del menu.

        :return: None
        """
        while True:
            opcion = input("Seleccione una opcion:\n1-Mostrar Reactivos\n2-Agregar\n3-Eliminar\n4-Editar\n5-salir\n--->")
            if opcion == "1":
                listar_reactivos(self.reactivos)
            elif opcion == "2":
                crear_reactivo(self.reactivos)
            elif opcion == "3":
                eliminar_reactivo(self.reactivos)
            elif opcion == "4":
                editar_reactivo(self.reactivos)
            elif opcion == "5":
                break
            else:
                print("Opcion invalida por favor introduzca solo uno de los valores dados--->")
    def menu_experimento(self):
        """
        Menu que se encarga de mostrar las opciones relacionadas con los experimentos,
        se encarga de redirigir a los diferentes menus segun la opcion seleccionada.

        Muestra las opciones para mostrar las recetas, mostrar los experimentos,
        eliminar experimentos, editar experimentos, realizar un experimento o salir del menu.

        :return: None
        """
        
        while True:
            opcion = input("Seleccione una opcion:\n1-Mostrar Recetas\n2-Mostrar experimentos\n3-Eliminar Experimentos\n4-Editar Experimentos\n5-Realizar experimento\n6-salir\n--->")
            if opcion == "1":
                mostrar_recetas(self.recetas)
                
            elif opcion == "2":
                mostrar_experimentos(self.experimentos)
                
            elif opcion == "3":
                eliminar_experimentos(self.experimentos)
                
            elif opcion == "4":
                editar_experimentos(self.experimentos)
            
            
            elif opcion == "5":
                for x in self.reactivos:
                    x.mostrar()
                realizar_experimento(self.recetas, self.reactivos, self.experimentos)
                
            elif opcion == "6":
                break
            else:
                print("Opcion invalida por favor introduzca solo uno de los valores dados--->")
    
    

    def obtener_api(self,url):
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
    def obtener_datos(self, archivo):
        """
        Abre el archivo especificado y devuelve los datos guardados en formato json.
        Parameters
        ----------
        archivo : str
            El nombre del archivo que se va a abrir y leer.
        Returns
        -------
        datos : list or dict
            Los datos guardados en el archivo en formato json.
        """
        with open(archivo, "r") as file:
            datos = json.load(file)
        file.close()
        return datos

    def guardar(self):
        """
        Guarda los datos de los experimentos, recetas y reactivos en archivos json locales.
        
        """
        
        with open("experimentos.json","w", encoding="utf-8") as file:
            lista = []
            for x in self.experimentos:
                lista.append(x.guardar_experimento())
            json.dump(lista,file)
            file.close()
            
        with open("recetas.json","w", encoding="utf-8") as file:
            lista = []
            for x in self.recetas:
                lista.append(x.guardar_receta())
            json.dump(lista,file)
            file.close()
            
        with open("reactivos.json", "w", encoding = "utf-8") as file:
            lista = []
            for x in self.reactivos:
                
                lista.append(x.guardar_reactivo())
            json.dump(lista,file)
            file.close()       
        
    def carga_inicial(self):
        """
        Carga los datos de los reactivos, experimentos y recetas desde el repositorio github.
        """
        
        datos_reactivos = self.obtener_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json")
        reacts = datos_reactivos
        
        for reactivo in reacts:
            id = reactivo["id"]
            nombre = reactivo["nombre"]
            descripcion = reactivo["descripcion"]
            costo = reactivo["costo"]
            categoria = reactivo["categoria"]
            inventario = reactivo["inventario_disponible"]
            unidad_medicion = reactivo["unidad_medida"]
            fecha_caducidad = reactivo["fecha_caducidad"]
            minimo_sugerido = reactivo["minimo_sugerido"]
            conversiones_posibles = reactivo["conversiones_posibles"]
        
            reactivo = reac(id,nombre, descripcion, costo, categoria, inventario, unidad_medicion,fecha_caducidad,minimo_sugerido,conversiones_posibles)
            self.reactivos.append(reactivo)
        
            
        datos_experimento = self.obtener_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json")
        expe = datos_experimento
        for experimento in expe:
            id = experimento["id"]
            receta_id = experimento["receta_id"]
            responsables = experimento["personas_responsables"]
            fecha = experimento["fecha"]
            costo = experimento["costo_asociado"]
            resultado = experimento["resultado"]
            obejeto_experimento = ex(id, receta_id,  fecha, responsables, costo, resultado)
            self.experimentos.append(obejeto_experimento)
        
        datos_recetas = self.obtener_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/recetas.json")
        for receta in datos_recetas:
            id = receta["id"]
            nombre = receta["nombre"]
            objetivo = receta["objetivo"]
            reactivos_utilizados = receta["reactivos_utilizados"]
            procedimiento = receta["procedimiento"]
            for j in reactivos_utilizados:
                id_reactivo = j["reactivo_id"]
                cantidad_necesaria = j["cantidad_necesaria"]
                unidad_medida = j["unidad_medida"]
                reactivo_u = ReactivoUtilizado(id_reactivo, cantidad_necesaria, unidad_medida)
                self.reactivo_utilizado.append(reactivo_u)
            valores_a_medir = receta["valores_a_medir"]
            
            for k in valores_a_medir:
                nombre_valores = k["nombre"]
                formula = k["formula"]
                minimo = k["minimo"]
                maximo = k["maximo"]
                objeto_valores = Valores_medir(nombre_valores,formula,minimo,maximo)
                self.valores_medir.append(objeto_valores)
                
            objeto_receta = rec(id,nombre,objetivo,reactivos_utilizados,procedimiento,valores_a_medir)
            self.recetas.append(objeto_receta)
    
    def carga_normal(self):
        """
        Metodo que carga los datos de los reactivos, experimentos y recetas desde archivos locales.
        """
        
        datos_reactivos = self.obtener_datos("reactivos.json")
        reacts = datos_reactivos
            
        for reactivo in reacts:
            id = reactivo["id"]
            nombre = reactivo["nombre"]
            descripcion = reactivo["descripcion"]
            costo = reactivo["costo"]
            categoria = reactivo["categoria"]
            inventario = reactivo["inventario_disponible"]
            unidad_medicion = reactivo["unidad_medida"]
            fecha_caducidad = reactivo["fecha_caducidad"]
            minimo_sugerido = reactivo["minimo_sugerido"]
            conversiones_posibles = reactivo["conversiones_posibles"]
            
            reactivo = reac(id,nombre, descripcion, costo, categoria, inventario, unidad_medicion,fecha_caducidad,minimo_sugerido,conversiones_posibles)
            self.reactivos.append(reactivo)
                
        datos_experimento = self.obtener_datos("experimentos.json")
        expe = datos_experimento
        for experimento in expe:
            id = experimento["id"]
            receta_id = experimento["receta_id"]
            responsables = experimento["personas_responsables"]
            fecha = experimento["fecha"]
            costo = experimento["costo_asociado"]
            resultado = experimento["resultado"]

            obejeto_experimento = ex(id, receta_id,  fecha, responsables, costo, resultado)
            self.experimentos.append(obejeto_experimento)
            
        datos_recetas = self.obtener_datos("recetas.json")
        for receta in datos_recetas:
            id = receta["id"]
            nombre = receta["nombre"]
            objetivo = receta["objetivo"]
            reactivos_utilizados = receta["reactivos_utilizados"]
            procedimiento = receta["procedimiento"]
            
            for j in reactivos_utilizados:
                id_reactivo = j["reactivo_id"]
                cantidad_necesaria = j["cantidad_necesaria"]
                unidad_medida = j["unidad_medida"]
                reactivo_u = ReactivoUtilizado(id_reactivo, cantidad_necesaria, unidad_medida)
                self.reactivo_utilizado.append(reactivo_u)
            valores_a_medir = receta["valores_a_medir"]
            
            for k in valores_a_medir:
                nombre_valores = k["nombre"]
                formula = k["formula"]
                minimo = k["minimo"]
                maximo = k["maximo"]
                objeto_valores = Valores_medir(nombre_valores,formula,minimo,maximo)
                self.valores_medir.append(objeto_valores)
                
            objeto_receta = rec(id,nombre,objetivo,reactivos_utilizados,procedimiento,valores_a_medir)
            self.recetas.append(objeto_receta)
            
    def estadisticas(self):
        """
        Muestra las estadisticas del laboratorio de Quimica.
        Selecciona una opcion para ver las estadisticas deseadas.
        """
        
        while True:
            opcion = input("Seleccione una opción: \n1-Ver investigadores que más utilizan el laboratorio\n2-Revisar experimento más hecho y menos hecho\n3-Determinar los 5 reactivos con más alta rotación\n4-Determinar los 3 reactivos con mayor desperdicio\n5-Determinar los reactivos que más se vencen\6-Determinar cuantas veces no se logró hacer un experimento por falta de reactivos\n7-salir\n---->")
            if opcion == "1":
                diccio = {}
                for experimento in self.experimentos:
                    for persona in experimento.responsables:
                        if persona not in diccio.keys():
                            diccio[persona] = 1
                        else:
                            diccio[persona] += 1
                            
                diccio = dict(sorted(diccio.items(), key=lambda item: item[1], reverse=True))
                print("Personas que más han utilizado el laboratorio de mayor a menor:")
                print(diccio)
            elif opcion == "2":
                diccio = {}
                for experimento in self.experimentos:
                    for receta in self.recetas:
                        if receta.id == experimento.receta_id and receta.nombre not in diccio.keys():
                            diccio[receta.nombre] = 1
                        elif receta.id == experimento.receta_id:
                            diccio[receta.nombre] += 1
                diccio = dict(sorted(diccio.items(), key=lambda item: item[1], reverse=True))
                print("Experimentos realizados:")
                print(diccio)
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass