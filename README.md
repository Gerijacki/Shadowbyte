# Shadowbyte

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9+-yellow)

**Shadowbyte** es un kit de herramientas profesional para administradores de sistemas, entusiastas de redes y desarrolladores. Diseñado para ser modular, rápido y fácil de usar desde la línea de comandos.

## 🚀 Características

- **🖥️ Sistema**: Monitorización en tiempo real (CPU, RAM, Disco), limpieza de temporales, actualizaciones del sistema.
- **🌐 Red**: Test de velocidad, escáner de red local (LAN), información de interfaces y IP pública.
- **🔐 Seguridad**: Generador de contraseñas seguras, escáner de archivos con VirusTotal.
- **📁 Archivos**: Comparación de directorios, **encriptación/desencriptación AES**.
- **🎥 Media**: Descarga de videos de YouTube (yt-dlp), generador de códigos QR.
- **✅ Tareas**: Gestor de tareas ligero integrado.

## 📦 Instalación

### Opción 1: Instalación Local (Python)

Recomendado si quieres usarlo como herramienta diaria en tu sistema.

```bash
# Clonar el repositorio
git clone https://github.com/gerijacki/shadowbyte.git
cd shadowbyte

# Crear entorno virtual (opcional pero recomendado)
python3 -m venv venv
source venv/bin/activate

# Instalar
pip install .
```

### Opción 2: Docker 🐳

Ideal para probar la herramienta sin instalar dependencias en tu sistema.

```bash
# Construir la imagen
docker build -t shadowbyte .

# Ejecutar (Ejemplo para ver la ayuda)
docker run --rm shadowbyte --help

# Ejecutar Monitor de Sistema (requiere flags especiales para acceder al host)
docker run --rm -it --pid=host shadowbyte system monitor
```

## 🛠️ Uso

Shadowbyte utiliza una estructura de comandos intuitiva: `shadowbyte [CATEGORIA] [COMANDO]`

### Comandos Principales

#### Sistema

```bash
# Ver información del sistema
shadowbyte system info

# Monitor en tiempo real (CPU/RAM/Red)
shadowbyte system monitor

# Limpiar archivos temporales
shadowbyte system clean
```

#### Red

```bash
# Escanear red local (requiere permisos de administrador/root)
sudo shadowbyte network scan --range 192.168.1.1/24

# Test de velocidad de internet
shadowbyte network speedtest
```

#### Seguridad y Archivos

```bash
# Generar contraseña segura de 20 caracteres
shadowbyte security password --length 20

# Encriptar un archivo (genera 'secret.key' si no existe)
shadowbyte files encrypt mis_secretos.txt

# Desencriptar
shadowbyte files decrypt mis_secretos.txt.enc
```

#### Media

```bash
# Descargar video de YouTube
shadowbyte media yt "https://youtube.com/watch?v=..."

# Generar código QR
shadowbyte media qr "https://github.com/gerijacki" --output mi_qr.png
```

## ⚙️ Configuración

Algunas funciones (como VirusTotal) requieren configuración.

```bash
# Ver configuración actual
shadowbyte security config

# Configurar API Key de VirusTotal
shadowbyte security config --key virustotal_api_key --value "TU_API_KEY"
```

Los datos se guardan en `config.json`.

## 📄 Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).

---

Creado por **Gerijacki**.
