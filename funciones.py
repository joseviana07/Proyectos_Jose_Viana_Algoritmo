from datetime import datetime
from experimento import Experimento
from reactivo import Reactivo
def crear_reactivo(reactivos):
    """
    Crea un nuevo reactivo y lo agrega a la lista de reactivos.
    Pide al usuario el id, nombre, descripción, costo, categoría, inventario, unidad de medida y fecha de caducidad del reactivo.
    Valida que el id sea un número, el nombre y la descripción sean cadenas de texto, el costo sea un número con decimales, la categoría sea una cadena de texto, el inventario sea un número entero, la unidad de medida sea una de las opciones (mL,L,uL,g,mg,kg) y la fecha de caducidad sea una fecha en formato AAAA-MM-DD.
    Si el usuario introduce un valor inválido, se le pedirá que lo corrija.
    """
    id = len(reactivos)+1
    nombre = input("Ingrese el nombre del reactivo: ")
    while not nombre.strip():  
        print("El nombre del reactivo es obligatorio.")
        nombre = input("Ingrese el nombre del reactivo: ")

    descripcion = input("Ingrese la descripción del reactivo: ")

    costo = input("Ingrese el costo del reactivo: ")
    while not costo.replace(".", "", 1).isdigit():  
        print("El costo es invalido.")
        costo = input("Ingrese el costo del reactivo: ")

    categoria = input("Ingrese la categoría del reactivo: ")
    while not categoria.strip():  
        print("La categoría del reactivo es obligatoria.")
        categoria = input("Ingrese la categoría del reactivo: ")

    inventario = input("Ingrese el inventario del reactivo: ")
    while not inventario.isnumeric() or int(inventario) < 0:
        print("El inventario del reactivo debe ser un númerero entero.")
        inventario = input("Ingrese el inventario del reactivo: ")

    unidad_medida = input("Ingrese la unidad de medida del reactivo:(mL,L,uL,g,mg,kg) ")
    while unidad_medida not in ["mL", "L", "uL", "g", "mg", "Kg"]:  
        print("La unidad de medida del reactivo no es válida.")
        unidad_medida = input("Ingrese la unidad de medida del reactivo:(mL,L,uL,g,mg,kg) ")

    año = input("Ingrese el año de expiración: ")
    while not año.isnumeric() or int(año) < 2025:
        año = input("Ingrese el año de expiración: ")

    mes = input("Ingrese el mes de expiración (1-12): ")
    while not mes.isnumeric() or int(mes) not in range(1, 13):
        mes = input("Ingrese el mes de expiración (1-12): ")
    if len(mes) == 1:
        mes = "0" + mes

    dia = input("Ingrese el día de expiración: ")
    while not dia.isnumeric() or (mes == "02" and not int(DeprecationWarning) in range(1, 28)) or (mes in ["01", "03", "05", "07", "08", "10", "12"] and not int(dia) in range(1, 31)) or (mes in ["04", "06", "09", "11"] and not int(dia) in range(1, 30)):
        dia = input("Ingrese el día de expiración: ")
    if len(dia) == 1:
        dia = "0" + dia

    fecha_caducidad = f"{año}-{mes}-{dia}"
    minimo_sugerido = input("Ingrese el minimo sugerido del reactivo: ")
    while not minimo_sugerido.isnumeric() or int(minimo_sugerido) < 0:
        print("El minimo sugerido del reactivo debe ser un número entero no negativo.")
        minimo_sugerido = input("Ingrese el minimo sugerido del reactivo: ")

    conversiones_posibles = input("Ingrese las conversiones posibles del reactivo: ")
    while not conversiones_posibles.strip():  
        print("Las conversiones posibles del reactivo son obligatorias.")
        conversiones_posibles = input("Ingrese las conversiones posibles del reactivo: ")

    reactivo = Reactivo(id,nombre, descripcion, costo, categoria, inventario, unidad_medida,fecha_caducidad,minimo_sugerido,conversiones_posibles)
    reactivos.append(reactivo)
    print("Reactivo creado con éxito.")
def eliminar_reactivo(reactivos):
    """Elimina un reactivo de la lista de reactivos."""
    reactivo_id = int(input("Introduce el id del reactivo a eliminar---->"))
    for i in reactivos:
        if i.id == reactivo_id:
            reactivos.remove(i)
            break
    return reactivos

def listar_reactivos(reactivos):
    """Muestra todos los reactivos de la lista de reactivos.
    Por cada reactivo, se muestra su nombre, descripcion, costo, categoria, inventario, unidad de medida y fecha de caducidad.
    """
    for i in reactivos:
        i.mostrar()

def editar_reactivo(reactivos):
    """Edita un reactivo de la lista de reactivos."""
    reactivos_busqueda = input("\nIngrese el id del reactivo a editar: ")
    while not reactivos_busqueda.isnumeric():
        reactivos_busqueda = input("\nIngrese un ID valido para el reactivo a editar: ")

    for reactivo in reactivos:
        if int(reactivos_busqueda) == reactivo.id:
            print(reactivo.mostrar())

    option = input("\n¿Qué quieres editar?\n\n1. Nombre.\n2. Descripción.\n3. Costo.\n4. Categoría.\n5. Inventario.\n6. Unidad.\n7. Fecha de caducidad.\n8. Mínimo sugerido.\n\n>> ")
    while not option.isnumeric() or int(option) not in range(1,9):
        option = input("\n¿Qué quieres editar?\n\n1. Nombre.\n2. Descripción.\n3. Costo.\n4. Categoría.\n5. Inventario.\n6. Unidad.\n7. Fecha de caducidad.\n8. Mínimo sugerido.\n\n>> ")

    for reactivo in reactivos:
        if int(reactivos_busqueda) == reactivo.id:
            if option == "1": 
                nuevo_nombre = input("\nIngrese un nombre: ")
                reactivo.nombre = nuevo_nombre 

            elif option == "2": 
                new_description = input("\nIngrese una descripción: ")
                reactivo.descripcion = new_description 

            elif option == "3": 
                new_cost = input("\nIngrese un costo: $") 
                valid_new_cost = False 
                while not valid_new_cost:
                    try:
                        float(new_cost)
                        if float(new_cost) > 0:
                            valid_new_cost = True
                        else:
                            new_cost = input("Ingrese un costo válido: $")
                    except ValueError:
                        new_cost = input("Ingrese un costo válido: $")
                reactivo.costo = float(new_cost) 

            elif option == "4": 
                new_category = input("\nIngrese una categoría: ")
                reactivo.categoria = new_category
    
            elif option == "5": 
                new_stock = input("\nInventario: ") 
                valid_new_stock = False
                while not valid_new_stock:
                    try:
                        float(new_stock)
                        if float(new_stock) > 0:
                            valid_new_stock = True
                        else:
                            new_stock = input("Ingrese una cantidad de inventario válida: ")
                    except ValueError:
                        new_stock = input("Ingrese una cantidad de inventario válida: ")
                reactivo.inventario = float(new_stock) 

            elif option == "6":
                new_unit = input("\nIngrese una unidad de medida: ")
                reactivo.unidad_medicion = new_unit

            elif option == "7":
                year = input("- Año: ")
                while not year.isnumeric() or int(year) < 2025:
                    year = input("- Año: ")
                month = input("- Mes: ")
                while not month.isnumeric() or int(month) not in range(1, 13):
                    month = input("- Mes: ")
                
                if len(month) == 1:
                    month = "0" + month
                day = input("- Día: ")
                while not day.isnumeric() or (month == "2" and not int(day) in range(1,28) ) or (month in ["1", "3", "5", "7", "8", "10", "12"] and not int(day) in range(1, 31)) or (month in ["4", "6", "9", "11"] and not int(day) in range(1, 30)):
                    day = input("- Día: ")
                
                if len(day) == 1:
                    day = "0" + day
                new_expiration_date = f"{year}-{month}-{day}"
                reactivo.fecha_caducidad = new_expiration_date 

            elif option == "8":
                new_minimum_suggested = input("\nMínimo sugerido: ") 
                valid_new_min = False
                while not valid_new_min:
                    try:
                        float(new_minimum_suggested)
                        if float(new_minimum_suggested) >= 0:
                            valid_new_min = True
                        else:
                            new_minimum_suggested = input("Ingrese un mínimo sugerido válido: ")
                    except ValueError:
                        new_minimum_suggested = input("Ingrese un mínimo sugerido válido: ")
                reactivo.minimo_sugerido = float(new_minimum_suggested) 


def revisar(reactivos):
    """
    Revisa si el inventario de cada reactivo es menor al minimo sugerido, y
    muestra un mensaje de alerta en caso de ser cierto.
    
    Parameters:
    reactivos (list): lista de objetos tipo Reactivo
    """
    for reactivo in reactivos:
        if reactivo.inventario < reactivo.minimo_sugerido:
            print(f"ALERTA, inventario de {reactivo.nombre} es menor al minimo sugerido.")
def mostrar_recetas (recetas):
    """
    Muestra las recetas en la lista de recetas.

    Parameters:
    recetas (list): lista de objetos tipo Receta
    """
    for receta in recetas:
        receta.mostrar()
        
def mostrar_experimentos(experimentos):
    """
    Muestra los experimentos en la lista de experimentos.

    Parameters:
    experimentos (list): lista de objetos tipo Experimento
    """
    for experimento in experimentos:
        experimento.mostrar()


def realizar_experimento(recetas, reactivos, experimentos):
    """
    Realiza un experimento utilizando una receta seleccionada, actualiza el inventario de reactivos,
    evalúa los resultados del experimento y lo agrega al registro de experimentos.
    Parameters:
    recetas (list): lista de objetos tipo Receta disponibles para realizar el experimento.
    reactivos (list): lista de objetos tipo Reactivo disponibles en el inventario.
    experimentos (list): lista de objetos tipo Experimento donde se registran los experimentos realizados.
    Returns:
    bool: False si el experimento no es realizable por falta de inventario o reactivos vencidos.
    """

    numero = input("Introduzcan cuantas personas participarán en el experimento---->")
    while not numero.isnumeric():   
        numero = input("Introduzca un numero valido---->")
    encargados = []
    for x in range(int(numero)):
        investigadores = input("Introduzca el nombre del encargado del experimento--->")
        while investigadores == "":
            investigadores = input("Introduzca el nombre del encargado del experimento--->")
        encargados.append(investigadores)
    mostrar_recetas(recetas)
    expe = input("Introduzca el id de la receta a utilizar---->")
    for receta in recetas:
        if receta.id == int(expe):
            valores = receta.realizar(reactivos)
            if valores == False:
                print(valores)
                print("Experimento no disponible por falta de inventario o reactivos vencidos.")
                return False
        
            lista_id = [x.id for x in experimentos]
            var = len(lista_id)+1
                
                
            evaluar = receta.valores_medir
            resultado = ""
            for y in evaluar:
                print(y)
                valor = y["nombre"]
                x = input(f"Introduzca el valor final para {valor}---->")
                if int(x) <= y["maximo"] and int(x) >= y["minimo"]:
                    resultado += f"Valor de {valor} aceptado."
                else:
                    resultado += f"Valor de {valor} fallido."
            fecha = datetime.now()
            fecha = fecha.strftime("%Y-%m-%d")
            nuevo = Experimento(var, receta.id, fecha, encargados, valores,resultado )
    experimentos.append(nuevo)
    print("Experimento agregado al registro de experimentos")
    
def eliminar_experimentos(experimentos):
    """
    Muestra la lista de experimentos y pide el id del experimento a eliminar.
    Si el id coincide con alguno de los experimentos, lo elimina de la lista de experimentos.
    """
    
    for experimento in experimentos:
        experimento.mostrar()
    
    id_experimento = input("Introduce el id del experimento a eliminar-->")
    for experimento in experimentos:
        if experimento.id == int(id_experimento):
            experimentos.remove(experimento)
    print("Experimento eliminado con éxito")

def editar_experimentos(experimentos):
    """
    Muestra la lista de experimentos y pide el id del experimento a editar.
    Segun la opcion que elija, edita los responsables del experimento, la fecha o el resultado.
    """
    
    for experimento in experimentos:
        experimento.mostrar()
    
    
    while True:
        decision = input("Introduce alguna de las opciones:\n1-Editar personas responsables\n2-Editar fecha\n3-Resultado\n4-Salir\n--->")
        
        if decision == "1":
            personas = []
            numero = input("Introduzca el numero de personas responsables de el experimento----->")
            id_experimento = input("Introduce el id del experimento a editar------>")
            for experimento in experimentos:
                if experimento.id == int(id_experimento):
                    for i in range(int(numero)):
                        persona = input("Introduce el nombre------>")
                        personas.append(persona)
                    experimento.responsables = personas
                    
        elif decision == "2":
            id_experimento = input("Introduce el id del experimento a editar------>")
            for experimento in experimentos:
                if experimento.id == int(id_experimento):
                    fecha = input("Introduce la fecha con el siguiente formato: (YYYY-MM-DD)------>")
                    experimento.fecha = fecha
        elif decision == "3":
            id_experimento = input("Introduce el id del experimento a editar------>")
            for experimento in experimentos:
                if experimento.id == int(id_experimento):
                    resultado = input("Introduce el nuevo resultado------>")
                    experimento.resultado = resultado
        elif decision == "4":
            break
        else:
            print("Por favor solo introduzca una opción válida")
                