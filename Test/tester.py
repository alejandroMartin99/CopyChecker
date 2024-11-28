import os
from fpdf import FPDF

# Lista fija de empleados (nombre completo)
EMPLEADOS = [
    "Alejandro García", "Beatriz Martínez", "Carlos López", "Diana Hernández", 
    "Eduardo Pérez", "Fernanda González", "Gabriel Rodríguez", "Hilda Sánchez", 
    "Ignacio Ramírez", "Julia Flores", "Karla Torres", "Luis Díaz", 
    "Mariana Cruz", "Nicolás Morales", "Oscar Vargas", "Paola Jiménez", 
    "Quintín Ortiz", "Raquel Castillo", "Sofía Reyes", "Tomás Gutiérrez"
]

# Lista fija de proyectos de ingeniería aeroespacial (siglas clave y descripción)
PROYECTOS = {
    "SNAO": "Sistema de Navegación Autónoma Orbital",
    "DCR": "Desarrollo de Cohetes Reutilizables",
    "PHS": "Propulsión Híbrida para Satélites",
    "SFE": "Simulación de Vuelos Espaciales",
    "MHL": "Módulos de Hábitat Lunar",
    "VH": "Vehículos Hipersónicos",
    "SRO": "Estaciones de Reabastecimiento en Órbita",
    "SAD": "Sistemas Anticolisión para Drones Espaciales",
    "AAAR": "Análisis Aerodinámico para Reingreso Atmosférico",
    "DSGZ": "Diseño de Sensores de Gravedad Zero"
}

# Lista fija de meses y años
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

ANIOS = ["2023", "2024"]

# Generación de PDFs organizada por proyectos
def organizar_por_proyectos(base_path):
    """
    Genera una estructura donde las nóminas están organizadas por proyectos.
    """
    for sigla, descripcion in PROYECTOS.items():
        proyecto_path = os.path.join(base_path, sigla)
        os.makedirs(proyecto_path, exist_ok=True)

        for empleado in EMPLEADOS:
            empleado_path = os.path.join(proyecto_path, empleado)
            os.makedirs(empleado_path, exist_ok=True)

            for anio in ANIOS:
                for mes in MESES:
                    archivo_pdf = os.path.join(
                        empleado_path, f"{sigla}_{empleado}_{anio}_{mes}.pdf"
                    )
                    generar_pdf(archivo_pdf, empleado, descripcion, sigla, anio, mes)
    print(f"Nóminas organizadas por proyectos en '{base_path}'.")

# Generación de PDFs organizada por meses
def organizar_por_meses(base_path):
    """
    Genera una estructura donde las nóminas están organizadas por meses.
    """
    for anio in ANIOS:
        for mes in MESES:
            mes_path = os.path.join(base_path, f"{anio}_{mes}")
            os.makedirs(mes_path, exist_ok=True)

            for sigla, descripcion in PROYECTOS.items():
                for empleado in EMPLEADOS:
                    archivo_pdf = os.path.join(
                        mes_path, f"{sigla}_{empleado}_{anio}_{mes}.pdf"
                    )
                    generar_pdf(archivo_pdf, empleado, descripcion, sigla, anio, mes)
    print(f"Nóminas organizadas por meses en '{base_path}'.")

# Función para generar un PDF
def generar_pdf(ruta, empleado, descripcion, sigla, anio, mes):
    """
    Genera un archivo PDF con los datos especificados.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Nómina", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Empleado: {empleado}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Proyecto: {descripcion} ({sigla})", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Mes: {mes}, Año: {anio}", ln=True, align="C")
    pdf.output(ruta)

# Función para comparar archivos generados en ambas estructuras
def comparar_estructuras(path1, path2):
    """
    Compara los archivos generados en dos directorios diferentes.
    """
    archivos_path1 = set()
    for root, _, files in os.walk(path1):
        archivos_path1.update(files)

    archivos_path2 = set()
    for root, _, files in os.walk(path2):
        archivos_path2.update(files)

    if archivos_path1 == archivos_path2:
        print("¡Las estructuras son idénticas! Todos los archivos coinciden.")
    else:
        print("Las estructuras son diferentes.")
        print("Archivos únicos en la primera estructura:", archivos_path1 - archivos_path2)
        print("Archivos únicos en la segunda estructura:", archivos_path2 - archivos_path1)




# Ejecutar las funciones
ruta_base_proyectos = r"C:\Users\Alex\Documents\GitHub\CopyChecker\Test\01_Origen"
ruta_base_meses = r"C:\Users\Alex\Documents\GitHub\CopyChecker\Test\02_Destino"

organizar_por_proyectos(ruta_base_proyectos)
organizar_por_meses(ruta_base_meses)
