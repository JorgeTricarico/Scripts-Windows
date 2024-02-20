import os
import sys
from git import Repo
from urllib.parse import urlparse
import subprocess

def command_exists(command):
    return subprocess.call(["where", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def get_username_and_repo_from_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')

    if not path_parts:
        raise ValueError("URL no válida")

    if len(path_parts) >= 2:
        username = path_parts[0]
        repo_name = path_parts[1].split('/')[0]
        return username, repo_name
    else:
        return None, None

def clone_and_open_repo(url):
    username, repo_name = get_username_and_repo_from_url(url)

    if username and repo_name:
        repo_dir = os.path.join(os.getcwd(), repo_name)
        try:
            Repo.clone_from(f"https://github.com/{username}/{repo_name}", f"{username}/{repo_name}")
        except PermissionError as e:
            print(f"Error de permisos al clonar: {e}")
            return
        print(f"Repositorio clonado en: {repo_dir}")

        idea_command = 'idea'  # Cambia a la ruta correcta si es necesario
        if not command_exists(idea_command):
            print(f"El comando '{idea_command}' no se encuentra. Instala IntelliJ IDEA o configura la ruta correctamente.")
            return

        # Cambios aquí para abrir en otra ventana de PowerShell
        idea_start_repo = f"start powershell.exe -NoExit -Command {idea_command} .\\{username}\\{repo_name}"
        try:
            subprocess.run(idea_start_repo, shell=True)
        except FileNotFoundError as e:
            print(f"Error al abrir proyecto: Archivo no encontrado ({e})")
        except subprocess.CalledProcessError as e:
            print(f"Error al abrir proyecto: {e}")
        print(f"Proyecto abierto en IDEA en: {username}/{repo_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL_del_repositorio> [ruta_a_IDEA]")
        sys.exit(1)

    url_repo = sys.argv[1]

    try:
        clone_and_open_repo(url_repo)
    except ValueError as e:
        print(f"Error: {e}")
