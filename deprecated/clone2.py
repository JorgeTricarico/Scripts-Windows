import os
import sys
from git import Repo
from git.exc import GitCommandError
from urllib.parse import urlparse


def obtener_nombre_usuario_y_repositorio_desde_url(url):
    # Parsear la URL para obtener el nombre de usuario y el nombre del repositorio
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')

    if len(path_parts) >= 2:
        usuario = path_parts[0]
        # Obtener el nombre del repositorio sin extensiones u otras partes
        nombre_repositorio = path_parts[-1].split('/')[-1]
        return usuario, nombre_repositorio
    else:
        return None, None


def clonar_repositorio(url):
    # Obtener el nombre de usuario y el nombre del repositorio desde la URL
    username, repo_name = obtener_nombre_usuario_y_repositorio_desde_url(url)

    if username and repo_name:
        ruta_carpeta_destino = os.path.join(os.getcwd(), repo_name)

        try:
            # Clonar el repositorio en la carpeta de destino
            Repo.clone_from(f"https://github.com/{username}/{repo_name}", f"{username}/{repo_name}")
            print(f"Repositorio clonado en: {os.path.abspath(ruta_carpeta_destino)}")
        except GitCommandError as e:
            print(f"Error al clonar el repositorio: {e}")
    else:
        print("No se pudo obtener el nombre de usuario y el nombre del repositorio desde la URL.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL_del_repositorio>")
        sys.exit(1)

    url_repositorio = sys.argv[1]

    clonar_repositorio(url_repositorio)