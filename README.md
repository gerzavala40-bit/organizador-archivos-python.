# 📁 Organizador Automático de Archivos en Python

Este es un script de automatización desarrollado en Python que ayuda a mantener limpias y organizadas las carpetas del sistema (como la carpeta de Descargas o Escritorio) clasificando los archivos de forma automática según su formato o extensión.

---

### 🛠️ Desarrollo y Enfoque Técnico

El proyecto fue desarrollado utilizando **desarrollo asistido por Inteligencia Artificial (AI-assisted development)**. Mi rol se centró en:
- **Lógica de Clasificación:** Definir la estructura del diccionario de mapeo para agrupar extensiones comunes (Documentos, Imágenes, Videos, Comprimidos y Audio).
- **Gestión del Sistema de Archivos:** Implementar lógica para interactuar de forma segura con el sistema operativo usando los módulos nativos `os` y `shutil`.
- **Control de Conflictos:** Supervisar la integración de una función que evita la sobrescritura de archivos con nombres duplicados agregando sufijos numéricos.

---

### ⚙️ Características

- **Modularidad:** Estructurado en funciones independientes para validar rutas, crear directorios y mover elementos.
- **Clasificación Dinámica:** Soporta múltiples formatos y cuenta con una categoría genérica ("Otros") para extensiones no especificadas.
- **Seguridad:** No elimina ningún archivo, solo los reubica y gestiona colisiones de nombres de forma automatizada.

---

### 🚀 Cómo ejecutarlo

1. Descargar o clonar el repositorio.
2. Modificar la variable `CARPETA_OBJETIVO` con la ruta local que se desea organizar.
3. Ejecutar en la terminal:
   ```bash
   python organizador_archivos.py
