# Añadir colores a tu código Python

from colorama import Fore, Style

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
purple = Fore.MAGENTA
reset = Style.RESET_ALL

colors = {'red': red, 'green': green, 'blue': blue, 'yellow': yellow, 'purple': purple, 'reset': reset}

print(colors['blue'] +"\n--> HOLA, MUNDO <--\n" + colors['reset'])
