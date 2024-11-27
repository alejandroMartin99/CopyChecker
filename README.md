# CopyChecker

CopyChecker es una aplicación de escritorio desarrollada en Python utilizando `customtkinter`, que permite comparar archivos entre dos carpetas. Extrae todos los archivos, incluyendo los de subcarpetas, de una carpeta de origen y los compara con los archivos en una carpeta de destino. La aplicación clasifica los archivos en dos grupos: aquellos que ya existen en el destino y aquellos que no. Además, permite copiar los archivos que no existen en destino, replicando la estructura de directorios.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Cómo usar](#cómo-usar)
- [Capturas de pantalla](#capturas-de-pantalla)
- [Dependencias](#dependencias)


## Características

- Comparación recursiva de archivos entre dos carpetas.
- Clasificación de archivos en:
  - **Ficheros que coinciden**: aquellos que ya están presentes en la carpeta de destino.
  - **Ficheros que no coinciden**: aquellos que no están en la carpeta de destino.
- Posibilidad de copiar archivos que no existen en la carpeta de destino, manteniendo la misma estructura de directorios.
- Interfaz amigable y moderna con `customtkinter`.
- Modo oscuro por defecto para una experiencia visual más agradable.

## Instalación

### Requisitos previos

Asegúrate de tener Python 3.6 o superior instalado en tu sistema. Puedes verificar tu versión de Python ejecutando:

```bash
python --version


Paso 1: Clona el repositorio
```bash
git clone https://github.com/tu-usuario/CopyChecker.git