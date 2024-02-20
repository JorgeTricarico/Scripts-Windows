# clonepy.py

import sys
import subprocess

def main():
    script_path = r'C:\Script\clone.py'  # Reemplaza con la ruta correcta

    # Verificar si se proporcionó al menos un argumento
    if len(sys.argv) > 1:
        # Crear la cadena de comando con la ruta del script de Python y los argumentos proporcionados
        command = ['python', script_path] + sys.argv[1:]
        
        # Ejecutar el comando
        subprocess.run(command)
    else:
        print("Uso: python clonepy.py C:\Script\clone.py")

if __name__ == "__main__":
    main()
