# CopyChecker

CopyChecker es una aplicación de escritorio desarrollada en Python utilizando `customtkinter`, que permite comparar archivos entre dos carpetas. Extrae todos los archivos, incluyendo los de subcarpetas, de una carpeta de origen y los compara con los archivos en una carpeta de destino. La aplicación clasifica los archivos en dos grupos: aquellos que ya existen en el destino y aquellos que no. Además, permite copiar los archivos que no existen en destino, replicando la estructura de directorios.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Test](#test)
- [Capturas de Pantalla](#capturas-de-pantalla)


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

Paso 1: Instala las dependencias
```bash
pip install customtkinter


## Uso

1. **Seleccionar carpetas:** Usa los botones para elegir la carpeta de origen y la carpeta de destino.
2. **Analizar archivos:** Haz clic en "Analizar Ficheros" para comparar las carpetas.
3. **Revisar resultados:** Los archivos que coinciden y los que no coinciden se mostrarán en las listas correspondientes.
4. **Copiar archivos:** Haz clic en "Copiar Archivos No Coincidentes" para copiar los archivos faltantes a la carpeta de destino, replicando la estructura de directorios.

## Test

### Tests Implementados

- **Test de comparación:** Verifica que la comparación de archivos entre dos carpetas funcione correctamente, asegurando que los archivos coincidentes y no coincidentes sean identificados adecuadamente.
- **Test de copia:** Asegura que los archivos no coincidentes sean copiados correctamente al destino, replicando la estructura de directorios.
- **Test de interfaz:** Comprueba que la interfaz de usuario responda correctamente a las interacciones del usuario, como la selección de carpetas y la visualización de resultados.

Para ejecutar los tests, puedes utilizar un framework de pruebas como `unittest` o `pytest`. Los test están implementados en el archivo `test_copychecker.py`.

## Capturas de Pantalla

![Captura de pantalla de la interfaz](screenshot1.png)
