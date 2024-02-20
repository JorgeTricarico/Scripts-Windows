import os
import sys
from git import Repo
from urllib.parse import urlparse

def obtener_nombre_usuario_desde_url(url):
    # Parsear la URL para obtener el nombre de usuario y el nombre del repositorio
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    
    if len(path_parts) >= 2:
        return path_parts[0]
    else:
        return None

def clonar_repositorio(url):
    # Obtener el nombre de usuario desde la URL
    nombre_usuario = obtener_nombre_usuario_desde_url(url)

    if nombre_usuario:
        # Crear la carpeta con el nombre de usuario
        carpeta_usuario = os.path.join(os.getcwd(), nombre_usuario)
        os.makedirs(carpeta_usuario, exist_ok=True)

        # Clonar el repositorio dentro de la carpeta del usuario
        repo = Repo.clone_from(url, os.path.join(carpeta_usuario, "repositorio_clonado"))

        print(f"Repositorio clonado en: {repo.working_tree_dir}")
    else:
        print("No se pudo obtener el nombre de usuario desde la URL.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL_del_repositorio>")
        sys.exit(1)

    url_repositorio = sys.argv[1]

    clonar_repositorio(url_repositorio)

