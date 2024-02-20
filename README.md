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

## Clonar con clone_vsc.py alias clone_vsc

Este script hace lo mismo que clone.py solo que luego abre el proyecto en VS.
___

## Clonar con clone_idea.py alias clone_idea

Este script hace lo mismo que clone.py solo que luego abre el proyecto en Intellij, esta pensado principalmente para clonar y abrir proyectos de Java rapidamente.

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
***

## Agregar un Alias en PowerShell
Crea un alias para un script en PowerShell, permitiendo ejecutarlo con un nombre más corto y fácil de recordar.        

**Pasos**
1. Abra la consola de PowerShell.

2. Escriba el siguiente comando para crear un alias:
```
Set-Alias <NombreAlias> <RutaScript.py>
```

**Ejemplo**
```
Set-Alias clone C:\Scripts\clone.py
```

***

## Agregar el Path a la Variable de Entorno
Agregar la ruta de acceso en Windows a la carpeta que contiene sus scripts a la variable de entorno Path para que pueda ejecutarlos sin escribir la ruta completa.

**Pasos:**

1. Abra el Panel de control de Windows.

2. Seleccione "Sistema".

3. Haga clic en "Configuración avanzada del sistema".

4. En la pestaña "Avanzadas", haga clic en "Variables de entorno".

5. En la sección "Variables del sistema", busque la variable Path.

6. Haga clic en "Editar".

7. Al final del valor de la variable, agregue un punto y coma (;) seguido de la ruta completa a la carpeta que contiene sus scripts.

**Ejemplo:**

- C:\Scripts\

