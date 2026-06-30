# organizador_archivos.py
# Script para organizar automáticamente archivos de una carpeta según su tipo

import os
import shutil

# --- CONFIGURACIÓN ---
# Indicá acá la ruta de la carpeta que querés organizar
CARPETA_OBJETIVO = r"C:\Users\germa\Desktop\prueba"  # Cambiar según tu sistema operativo

# Diccionario que mapea cada extensión a la carpeta de destino correspondiente
# Podés agregar o modificar extensiones según tus necesidades
MAPA_EXTENSIONES = {
    # Documentos
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".doc": "Documentos",
    ".txt": "Documentos",
    ".xlsx": "Documentos",
    ".pptx": "Documentos",

    # Imágenes
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".webp": "Imagenes",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Comprimidos
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
}

# Carpeta para archivos cuya extensión no está mapeada arriba
CARPETA_OTROS = "Otros"


def obtener_carpeta_destino(extension):
    """
    Recibe la extensión de un archivo (ej: '.pdf') y devuelve
    el nombre de la subcarpeta donde debería ir.
    Si la extensión no está en el diccionario, va a 'Otros'.
    """
    # .get() busca la clave en el diccionario; si no la encuentra, usa el valor por defecto
    return MAPA_EXTENSIONES.get(extension.lower(), CARPETA_OTROS)


def crear_carpeta_si_no_existe(ruta_carpeta):
    """
    Verifica si una carpeta existe; si no, la crea.
    Evita errores al intentar mover archivos a una carpeta inexistente.
    """
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"📁 Carpeta creada: {ruta_carpeta}")


def organizar_carpeta(ruta_origen):
    """
    Función principal: recorre todos los archivos de la carpeta origen,
    detecta su extensión y los mueve a la subcarpeta correspondiente.
    """
    # Validamos que la carpeta exista antes de continuar
    if not os.path.isdir(ruta_origen):
        print(f"⚠️ La carpeta '{ruta_origen}' no existe. Verificá la ruta.")
        return

    # os.listdir() devuelve todos los nombres de archivos y carpetas dentro de ruta_origen
    elementos = os.listdir(ruta_origen)

    archivos_movidos = 0

    for nombre_elemento in elementos:
        ruta_completa = os.path.join(ruta_origen, nombre_elemento)

        # Saltamos las carpetas (incluidas las que ya creó este script en ejecuciones previas)
        if os.path.isdir(ruta_completa):
            continue

        # os.path.splitext separa el nombre del archivo de su extensión
        # Ejemplo: "informe.pdf" -> ("informe", ".pdf")
        _, extension = os.path.splitext(nombre_elemento)

        # Si el archivo no tiene extensión (extension == ""), lo mandamos a "Otros"
        if extension == "":
            nombre_subcarpeta = CARPETA_OTROS
        else:
            nombre_subcarpeta = obtener_carpeta_destino(extension)

        # Construimos la ruta completa de la subcarpeta de destino
        ruta_subcarpeta = os.path.join(ruta_origen, nombre_subcarpeta)
        crear_carpeta_si_no_existe(ruta_subcarpeta)

        # Ruta final donde quedará el archivo movido
        ruta_destino = os.path.join(ruta_subcarpeta, nombre_elemento)

        # Evitamos sobrescribir si ya existe un archivo con el mismo nombre en destino
        ruta_destino = evitar_sobrescritura(ruta_destino)

        # shutil.move() mueve el archivo de la ruta origen a la ruta destino
        shutil.move(ruta_completa, ruta_destino)
        print(f"✅ Movido: {nombre_elemento} → {nombre_subcarpeta}/")
        archivos_movidos += 1

    print(f"\n🎉 Proceso finalizado. Se movieron {archivos_movidos} archivo(s).")


def evitar_sobrescritura(ruta_destino):
    """
    Si ya existe un archivo con el mismo nombre en la carpeta destino,
    le agrega un sufijo numérico para no sobrescribirlo.
    Ejemplo: 'foto.jpg' -> 'foto_1.jpg' si 'foto.jpg' ya existe.
    """
    if not os.path.exists(ruta_destino):
        return ruta_destino  # No hay conflicto, devolvemos la ruta tal cual

    carpeta, nombre_archivo = os.path.split(ruta_destino)
    nombre_base, extension = os.path.splitext(nombre_archivo)

    contador = 1
    nueva_ruta = ruta_destino

    # Vamos probando nombre_1, nombre_2, etc. hasta encontrar uno libre
    while os.path.exists(nueva_ruta):
        nuevo_nombre = f"{nombre_base}_{contador}{extension}"
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)
        contador += 1

    return nueva_ruta


if __name__ == "__main__":
    print(f"🔍 Organizando archivos en: {CARPETA_OBJETIVO}\n")
    organizar_carpeta(CARPETA_OBJETIVO)