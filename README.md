# 🤖 Slack Salary Saver Bot

Este bot automatiza la captura de mensajes importantes (como notificaciones de salario) desde un canal privado o DM de Slack y los guarda ordenadamente en un archivo de Excel en OneDrive.


## 🚀 Instalación Rápida
1.  **Descarga el código:** Clona este repositorio o descarga el ZIP y extráelo en una carpeta.
2.  **Instala las dependencias:** Haz **doble clic** en el archivo `install.bat` incluido en la carpeta.
    *O instala manualmente: `pip install -r requirements.txt`*

---

## ⚙️ Configuración

### 1. Obtener Credenciales de Slack
Necesitas tus credenciales (`Bot Token`, `App Token`, `Channel ID`).
👉 **[Ver Guía Paso a Paso (PowerPoint)]**

Abre el archivo `salary_bot.py` con un editor de texto y actualiza esta sección con tus datos:

BOTTKN  = "bot token"
APPTKN = "app token"
CHNLID = "codigo" 
FILEPATH = r"el path donde guardaste tu excel"


Nota: Asegúrate de que FILEPATH sea la ruta correcta en tu PC.

### 2. Generar el Excel
Ejecuta este script una sola vez para crear el archivo con el formato correcto:

Bash python setup_excel.py


## 🔄 Configuración de Inicio Automático (Windows)
Para que el bot se ejecute solo cada vez que enciendas tu computadora, usa el archivo StartBot.bat que ya está incluido:

1. En la carpeta del proyecto, haz Click Derecho sobre el archivo StartBot.bat y selecciona "Crear acceso directo".
2. Presiona las teclas Windows + R en tu teclado.
3. Escribe el comando shell:startup y presiona Enter. (Se abrirá la carpeta de "Inicio" de Windows).
4. Arrastra el acceso directo que acabas de crear hacia esa carpeta.

¡Listo! ✅ Ahora verás una ventana negra indicando que el bot está activo cada vez que inicies sesión.

