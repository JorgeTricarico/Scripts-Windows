import subprocess
import sys

def eliminar_carpeta(ruta_relativa_o_absoluta):
    try:
        subprocess.run(['powershell', '-Command', f'Remove-Item -Path "{ruta_relativa_o_absoluta}" -Recurse -Force'])
        print(f'Carpeta {ruta_absoluta} eliminada con éxito.')
    except Exception as e:
        print(f'Error al intentar eliminar la carpeta {ruta_relativa_o_absoluta}: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ruta_relativa>")
    else:
        ruta_relativa_o_absoluta = sys.argv[1]
        eliminar_carpeta(ruta_relativa_o_absoluta)
