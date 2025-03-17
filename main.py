from app import App
def main():    
    """
    Punto de entrada del programa. Se encarga de crear una instancia de App y llamar a su
    metodo menu_principal, que es el encargado de mostrar las opciones principales del programa.
    """
    print("------------------------------------------------------------------------------BIENVENIDO------------------------------------------------------------------------------")
    app = App()
    app.menu_principal()
main()
3
