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
        repo_dir = os.path.join(os.getcwd(), username, repo_name)  # Actualización: ruta completa
        try:
            Repo.clone_from(f"https://github.com/{username}/{repo_name}", repo_dir)  # Actualización: ruta del destino
            os.chdir(repo_dir)  # Actualización: cambio de directorio
            subprocess.call(["C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", "."])  # Actualización: usando subprocess.call
        except PermissionError as e:
            print(f"Error de permisos al clonar: {e}")
            return
        print(f"Repositorio clonado y abierto con VSC en: {repo_dir}")  # Actualización: mensaje

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL_del_repositorio>")  # Actualización: sin ruta a IDEA
        sys.exit(1)

    url_repo = sys.argv[1]

    try:
        clone_and_open_repo(url_repo)
    except ValueError as e:
        print(f"Error: {e}")
