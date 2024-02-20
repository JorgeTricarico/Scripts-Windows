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
Repositorio clonado en: C:\Ruta\Usuario\Repositorio
```
**Estructura de Carpeta**
```bash
Usuario/
    └── Nombrerepositorio/
            └── Contenido del Repositorio Clonado
```
___

## Clonar con clone_idea.py alias clone_idea

Este script hace lo mismo que clone.py solo que luego abre el proyecto en Intellij, esta pensado principalmente para clonar y abrir proyectos de Java rapidamente

___

## Eliminar Carpeta y Contenido (`remove.py` alias `remove`)
Este script elimina una carpeta y su contenido dado un path relativo. Puede ser útil para limpiar directorios de forma automatizada.

**Uso:**
```bash
python remove.py <ruta_relativa_o_absoluta>
```
**Con Alias:**
```bash
Remove JorgeTricarico
```
**Salida:**
```
Carpeta JorgeTricarico eliminada con éxito.
```
