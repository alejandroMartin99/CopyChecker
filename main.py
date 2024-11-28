import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Función para listar archivos recursivamente
def listar_archivos(carpeta):
    archivos = []
    for root, dirs, files in os.walk(carpeta):
        for file in files:
            ruta_completa = os.path.join(root, file)
            archivos.append(ruta_completa)
    return archivos

# Función para obtener la ruta relativa del archivo respecto a la carpeta base
def obtener_ruta_relativa(archivo, carpeta_base):
    return os.path.relpath(archivo, carpeta_base)

# Función para comparar archivos entre origen y destino
def comparar_archivos(origen, destino):
    archivos_origen = listar_archivos(origen)
    archivos_destino = listar_archivos(destino)

    ficheros_a_sobrescribir = []
    ficheros_no_cruzan = []

    # Crear un set con los nombres de los archivos en destino (sin importar ruta)
    nombres_archivos_destino = {os.path.basename(archivo) for archivo in archivos_destino}

    for archivo_origen in archivos_origen:
        nombre_archivo_origen = os.path.basename(archivo_origen)

        # Si el archivo está en el set de nombres de destino, se considera que coincide
        if nombre_archivo_origen in nombres_archivos_destino:
            ficheros_a_sobrescribir.append(archivo_origen)
        else:
            ficheros_no_cruzan.append(archivo_origen)

    return ficheros_a_sobrescribir, ficheros_no_cruzan

# Función para copiar archivos que no están en destino, replicando la estructura de directorios
def copiar_archivos(ficheros, origen, destino):
    for fichero in ficheros:
        ruta_relativa = obtener_ruta_relativa(fichero, origen)
        ruta_destino = os.path.join(destino, ruta_relativa)

        # Verifica si el directorio de destino existe, si no lo crea
        ruta_directorio_destino = os.path.dirname(ruta_destino)
        if not os.path.exists(ruta_directorio_destino):
            os.makedirs(ruta_directorio_destino)

        # Verificar si el archivo existe antes de copiar
        if os.path.exists(fichero):
            shutil.copy2(fichero, ruta_destino)
        else:
            print(f"Archivo no encontrado: {fichero}")

# Función que ejecuta la comparativa
def analizar_ficheros():
    carpeta_origen = entrada_origen.get()
    carpeta_destino = entrada_destino.get()

    if not carpeta_origen or not carpeta_destino:
        messagebox.showerror("Error", "Por favor selecciona ambas carpetas.")
        return

    ficheros_a_sobrescribir, ficheros_no_cruzan = comparar_archivos(carpeta_origen, carpeta_destino)

    # Limpiar las cajas de texto
    caja_ficheros_coinciden.delete("1.0", ctk.END)
    caja_ficheros_no_coinciden.delete("1.0", ctk.END)

    # Mostrar los resultados
    for fichero in ficheros_a_sobrescribir:
        caja_ficheros_coinciden.insert(ctk.END, obtener_ruta_relativa(fichero, carpeta_origen) + "\n")
    
    for fichero in ficheros_no_cruzan:
        caja_ficheros_no_coinciden.insert(ctk.END, obtener_ruta_relativa(fichero, carpeta_origen) + "\n")

# Función para copiar los archivos que no están en destino
def copiar_archivos_no_coinciden():
    ficheros = caja_ficheros_no_coinciden.get("1.0", ctk.END).strip().split("\n")
    ficheros = [f for f in ficheros if f]  # Filtrar líneas vacías

    # Convertir los archivos a sus rutas completas
    ficheros_rutas_completas = [
        os.path.join(entrada_origen.get(), fichero) for fichero in ficheros
    ]
    
    copiar_archivos(ficheros_rutas_completas, entrada_origen.get(), entrada_destino.get())
    messagebox.showinfo("Éxito", "Archivos copiados correctamente.")

# Función para seleccionar carpeta origen
def seleccionar_carpeta_origen():
    ruta = filedialog.askdirectory()
    entrada_origen.delete(0, ctk.END)
    entrada_origen.insert(0, ruta)

# Función para seleccionar carpeta destino
def seleccionar_carpeta_destino():
    ruta = filedialog.askdirectory()
    entrada_destino.delete(0, ctk.END)
    entrada_destino.insert(0, ruta)

# Configuración de la aplicación con customtkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de color

# Construir la ventana principal
ventana = ctk.CTk()
ventana.title("Comparador de Archivos")
ventana.geometry("800x600")

# Título
titulo = ctk.CTkLabel(ventana, text="Comparador de Archivos", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

# Selección de carpetas
frame_seleccion = ctk.CTkFrame(ventana)
frame_seleccion.pack(pady=20, padx=20, fill="x")

label_origen = ctk.CTkLabel(frame_seleccion, text="Carpeta Origen:")
label_origen.grid(row=0, column=0, padx=10, pady=10)

entrada_origen = ctk.CTkEntry(frame_seleccion, width=400)
entrada_origen.grid(row=0, column=1, padx=10, pady=10)

boton_origen = ctk.CTkButton(frame_seleccion, text="Seleccionar", command=seleccionar_carpeta_origen)
boton_origen.grid(row=0, column=2, padx=10, pady=10)

label_destino = ctk.CTkLabel(frame_seleccion, text="Carpeta Destino:")
label_destino.grid(row=1, column=0, padx=10, pady=10)

entrada_destino = ctk.CTkEntry(frame_seleccion, width=400)
entrada_destino.grid(row=1, column=1, padx=10, pady=10)

boton_destino = ctk.CTkButton(frame_seleccion, text="Seleccionar", command=seleccionar_carpeta_destino)
boton_destino.grid(row=1, column=2, padx=10, pady=10)

# Botón para analizar ficheros
boton_analizar = ctk.CTkButton(ventana, text="Analizar Ficheros", command=analizar_ficheros)
boton_analizar.pack(pady=10)

# Cajas para mostrar los resultados
frame_resultados = ctk.CTkFrame(ventana)
frame_resultados.pack(pady=20, padx=20, fill="both", expand=True)

label_coinciden = ctk.CTkLabel(frame_resultados, text="Ficheros que coinciden:")
label_coinciden.grid(row=0, column=0, padx=10, pady=10)

label_no_coinciden = ctk.CTkLabel(frame_resultados, text="Ficheros que no coinciden:")
label_no_coinciden.grid(row=0, column=1, padx=10, pady=10)

caja_ficheros_coinciden = ctk.CTkTextbox(frame_resultados, width=350, height=200)
caja_ficheros_coinciden.grid(row=1, column=0, padx=10, pady=10)

caja_ficheros_no_coinciden = ctk.CTkTextbox(frame_resultados, width=350, height=200)
caja_ficheros_no_coinciden.grid(row=1, column=1, padx=10, pady=10)

# Botón para copiar los archivos que no coinciden
boton_copiar = ctk.CTkButton(ventana, text="Copiar Archivos No Coincidentes", command=copiar_archivos_no_coinciden)
boton_copiar.pack(pady=10)

ventana.mainloop()
