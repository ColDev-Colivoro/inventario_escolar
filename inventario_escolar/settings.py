"""
Configuración del proyecto Django para la gestión de inventario escolar.
Generado por 'django-admin startproject' usando Django 5.2.7.
"""

from pathlib import Path

# Construye rutas dentro del proyecto así: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de inicio rápido para desarrollo - no apta para producción
# Ver: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantén la clave secreta usada en producción en secreto!
SECRET_KEY = "django-insecure-1&zc%j2&t&_dne7&02wx_v783*^s+f0620ffwvuz*1ozi$#swo"

# ADVERTENCIA DE SEGURIDAD: ¡no ejecutes con debug activado en producción!
DEBUG = True

ALLOWED_HOSTS = []


# Definición de aplicaciones
# Aquí se registran todas las aplicaciones que forman parte del proyecto.
INSTALLED_APPS = [
    "django.contrib.admin",        # Panel de administración de Django
    "django.contrib.auth",         # Sistema de autenticación y autorización
    "django.contrib.contenttypes", # Framework de tipos de contenido
    "django.contrib.sessions",     # Soporte para sesiones de usuario
    "django.contrib.messages",     # Sistema de mensajes flash
    "django.contrib.staticfiles",  # Manejo de archivos estáticos (CSS, JS, imágenes)
    "inventario_escolar",          # Aplicación principal del proyecto (si se creó con este nombre)
    "equipos",                     # Aplicación para la gestión de equipos
]

# Middleware: Procesadores de peticiones HTTP
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuración de las URLs raíz del proyecto
ROOT_URLCONF = "inventario_escolar.urls"

# Configuración de plantillas
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], # Directorios adicionales para buscar plantillas
        "APP_DIRS": True, # Buscar plantillas dentro de los directorios 'templates' de las apps
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request", # Hace el objeto request disponible en las plantillas
                "django.contrib.auth.context_processors.auth", # Proporciona información de autenticación
                "django.contrib.messages.context_processors.messages", # Proporciona mensajes flash
            ],
        },
    },
]

# Aplicación WSGI para el servidor web
WSGI_APPLICATION = "inventario_escolar.wsgi.application"


# Base de datos
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Configuración para la base de datos por defecto (SQLite en este caso)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Motor de base de datos
        "NAME": BASE_DIR / "db.sqlite3",       # Ruta al archivo de la base de datos
    }
}


# Validación de contraseñas
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
# Define las reglas para la complejidad de las contraseñas de usuario
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internacionalización (soporte para múltiples idiomas)
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us" # Código de idioma por defecto (se puede cambiar a 'es-es' para español)

TIME_ZONE = "UTC" # Zona horaria por defecto

USE_I18N = True # Habilita la internacionalización

USE_TZ = True # Habilita el soporte para zonas horarias


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/" # URL base para servir archivos estáticos


# Tipo de campo de clave primaria por defecto
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField" # Tipo de campo de clave primaria automático
