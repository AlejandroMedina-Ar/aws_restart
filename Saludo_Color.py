
#Para usar colores instalar "colorama"
#Desde la consola ingresamos pip install colorama
# y lo importamos a nuestro codigo con: "from colorama import Fore, Style, init"


from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def Saludo():
    name = input(Fore.YELLOW + "Por favor ingrese su nombre: ")  # Texto en amarillo
    print("\n") 
    print("\n")
    print(Fore.GREEN + f"Hola, ¿cómo estás: {name}?")  # Texto en verde
    print(Style.BRIGHT + Fore.BLUE + "¡Es un placer saludarte!")  # Texto brillante y azul

Saludo()
