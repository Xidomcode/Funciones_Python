# Función para Cerrar el script cuando pulsas Ctrl + C

import signal, sys

print(colors['yellow'] + "\n[+] Pulsa Ctrl + C en cualquier momento para cerrar el script.\n" + colors['reset'])

def fin_programa(signal, frame):
    print(colors['red'] + "\n\n[+] Cerrando programa...\n" + colors['reset'])
    sys.exit(0) 

signal.signal(signal.SIGINT, fin_programa)
