# Scripts-Windows
Scripts personales utilizados para trabajos diarios en Windows.
***
## Clonar Repositorios y crear subcarpetas (`clone.py` alias `clone`)

Este script recibe una URL de un repositorio de GitHub y crea la estructura de carpetas correspondiente dentro de la carpeta actual antes de clonar el repositorio con `git clone`. Diseñado para clonar repositorios en general y facilitar su apertura en Visual Studio Code.

**Uso:**
```bash
python clone.py https://github.com/Usuario/Repositorio
```
**Con Alias:**
```bash
clone https://github.com/Usuario/Repositorio
```
**Salida:**
```
usuario/
    └── Nombrerepositorio/
            └── Contenido del Repositorio (clonado)
```
___

## Clonar con clone_idea.py alias clone_idea

Este script hace lo mismo que clone.py solo que luego abre el proyecto en Intellij, esta pensado principalmente para clonar y abrir proyectos de Java rapidamente
