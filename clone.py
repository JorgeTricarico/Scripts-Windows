import os
import sys
from git import Repo
from urllib.parse import urlparse

def obtener_nombre_usuario_y_repositorio_desde_url(url):
    # Parsear la URL para obtener el nombre de usuario y el nombre del repositorio
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')

    if len(path_parts) >= 2:
        usuario = path_parts[0]
        # Excluir cualquier ruta adicional después del nombre del repositorio
        repositorio = path_parts[1].split('/')[0]
        return usuario, repositorio
    else:
        return None, None

def clonar_repositorio(url):
    # Obtener el nombre de usuario y el nombre del repositorio desde la URL
    nombre_usuario, nombre_repositorio = obtener_nombre_usuario_y_repositorio_desde_url(url)

    if nombre_usuario and nombre_repositorio:
        # Clonar el repositorio en el directorio actual
        repo = Repo.clone_from(f"https://github.com/{nombre_usuario}/{nombre_repositorio}", f"{nombre_usuario}/{nombre_repositorio}")

        print(f"Repositorio clonado en: {repo.working_tree_dir}")
    else:
        print("No se pudo obtener el nombre de usuario y el nombre del repositorio desde la URL.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL_del_repositorio>")
        sys.exit(1)

    url_repositorio = sys.argv[1]

    clonar_repositorio(url_repositorio)
