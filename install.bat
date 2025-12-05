@echo off
echo ==========================================
echo 📦 INSTALADOR DE DEPENDENCIAS DEL BOT
echo ==========================================
echo.
echo Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no esta instalado o no se encuentra en el PATH.
    echo Por favor instala Python desde python.org
    pause
    exit
)

echo.
echo Instalando librerias necesarias (slack_bolt, openpyxl)...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ Hubo un error instalando las librerias.
    echo Revisa tu conexion a internet.
) else (
    echo.
    echo ✅ EXITO: Todas las librerias fueron instaladas correctamente.
    echo Ya puedes configurar y ejecutar el bot.
)

echo.
pause