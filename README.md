# Sistema de Gestión de Inventario - DataBios

Este proyecto es un Sistema de Gestión de Inventario para la librería **DataBios**, desarrollado en **Django (Python)**. Está configurado siguiendo las mejores prácticas de la industria para ser seguro, fácil de configurar localmente y listo para su despliegue continuo en **GitHub** y servidores en la nube (como Render, Railway o Heroku).

---

## 🚀 Características del Despliegue y Seguridad

El proyecto cuenta con las siguientes mejoras implementadas para su distribución y despliegue seguro:
1. **Variables de Entorno:** Toda la información sensible (como claves secretas de Django y credenciales de bases de datos) ha sido extraída de los archivos de código a un archivo `.env` local.
2. **Conexión de Base de Datos Dinámica:** Admite el uso de variables de entorno de PostgreSQL individuales o una URI unificada de base de datos (`DATABASE_URL`).
3. **Fallback Automático a SQLite:** Si el servidor PostgreSQL no está disponible o no responde (por ejemplo, al ejecutar pruebas locales rápidas o durante flujos de trabajo en **GitHub Actions**), el sistema de forma inteligente conmuta y utiliza una base de datos local **SQLite** (`db.sqlite3`), permitiendo que el proyecto compile y se ejecute sin dependencias externas obligatorias.
4. **Archivos Estáticos en Producción:** Utiliza **WhiteNoise** integrado en el middleware de Django para servir, comprimir y cachear de forma eficiente los archivos estáticos en producción, sin requerir servidores adicionales como Nginx.
5. **Servidor de Producción:** Incluye un archivo `Procfile` configurado para ejecutar la aplicación con el servidor web **Gunicorn** (estándar de producción en Linux).

---

## 🛠️ Instalación y Configuración Local

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/MaxsForocca/DATABios.git
cd DATABios
```

### 2. Configurar el Entorno Virtual
Crea un entorno virtual e instálale las dependencias necesarias:
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar en Windows (CMD)
.\venv\Scripts\activate.bat

# Activar en Linux/macOS
source venv/bin/activate
```

### 3. Instalar Dependencias
Instala los paquetes necesarios enumerados en el archivo raíz:
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Copia la plantilla de variables de entorno y renómbrala a `.env`:
```bash
cp .env.example .env
```
Abre el archivo `.env` y ajusta las variables según sea necesario:
*   `DJANGO_SECRET_KEY`: Una clave aleatoria y segura para producción.
*   `DJANGO_DEBUG`: Define si se ejecuta en modo depuración (`True` en desarrollo, `False` en producción).
*   `DJANGO_ALLOWED_HOSTS`: Dominios autorizados separados por comas (por defecto `*` o `localhost`).
*   `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Credenciales locales de PostgreSQL. Si el puerto especificado de PostgreSQL no está escuchando conexiones, el sistema usará SQLite automáticamente.

### 5. Aplicar Migraciones
Crea la estructura de la base de datos en tu entorno local o SQLite fallback:
```bash
python DATABIOS/manage.py migrate
```

### 6. Crear un Superusuario
Crea una cuenta administrativa para acceder al panel:
```bash
python DATABIOS/manage.py createsuperuser
```

### 7. Iniciar el Servidor de Desarrollo
```bash
python DATABIOS/manage.py runserver
```
La aplicación estará disponible en `http://127.0.0.1:8000/`.

---

## 🐳 Despliegue en la Nube (Render / Railway / Heroku)

Gracias a las configuraciones añadidas, el despliegue es muy sencillo:

1. **Vincular Repositorio:** Vincula tu repositorio de GitHub a tu cuenta de Render, Railway o Heroku.
2. **Definir Variables de Entorno:** Configura las siguientes variables de entorno en el panel de control de tu plataforma de alojamiento:
   *   `DJANGO_SECRET_KEY`: (Clave de seguridad de producción).
   *   `DJANGO_DEBUG`: `False` (Importante para rendimiento y seguridad).
   *   `DJANGO_ALLOWED_HOSTS`: `tu-app.onrender.com` (U otro dominio de producción).
   *   `DATABASE_URL`: La URI de conexión de la base de datos PostgreSQL provista por tu plataforma de base de datos (por ejemplo, `postgres://usuario:contraseña@host:puerto/bd`).
3. **Comando de Inicio (Start Command):**
   Las plataformas leerán automáticamente el archivo `Procfile`. En caso de requerir configuración manual, utiliza:
   ```bash
   gunicorn --chdir DATABIOS DATABIOS.wsgi:application
   ```
4. **Comando de Compilación / Construcción (Build Command):**
   ```bash
   pip install -r requirements.txt && python DATABIOS/manage.py collectstatic --noinput
   ```

---

## 🧪 Pruebas e Integración Continua (GitHub Actions)

El proyecto está listo para ejecutarse en GitHub Actions con un flujo de trabajo estándar de Django. Dado que utiliza el fallback dinámico a SQLite, no es necesario aprovisionar un servicio de base de datos de PostgreSQL en GitHub Actions para pruebas rápidas o verificaciones estáticas.

Un flujo básico de GitHub Actions (`.github/workflows/django.yml`) para verificar que el código compile y pase los test de Django sería:

```yaml
name: Django CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Django Checks
      run: |
        python DATABIOS/manage.py check
    - name: Run Migrations
      run: |
        python DATABIOS/manage.py migrate
```
