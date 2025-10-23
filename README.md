# Gestión de Inventario Escolar

Esta aplicación web, desarrollada con Django, permite gestionar el inventario de equipos tecnológicos en un colegio. Facilita el registro, consulta y administración de equipos, reemplazando la gestión manual en planillas.

## Caso de Uso

El Colegio Andes del Sur requiere una aplicación web para gestionar su inventario de equipos tecnológicos. Actualmente, la información se mantiene en planillas, lo que dificulta el control y la actualización de los datos. Esta aplicación busca centralizar y facilitar la administración de estos equipos.

## Requisitos Previos

*   Python 3.x instalado.
*   Django instalado (`pip install django`).

## Configuración del Proyecto

1.  **Crear el proyecto Django:**
    Si el proyecto `inventario_escolar` no existe, créalo con:
    ```bash
    django-admin startproject inventario_escolar
    ```
    Si ya existe, asegúrate de estar dentro del directorio `inventario_escolar`.

2.  **Crear la aplicación `equipos`:**
    Dentro del directorio raíz del proyecto (`inventario_escolar`), ejecuta:
    ```bash
    python manage.py startapp equipos
    ```
    *Nota: Si recibes un error indicando que el nombre `equipos` ya existe, puede que ya se haya creado. Verifica la estructura de directorios.*

3.  **Configurar `settings.py`:**
    Abre el archivo `inventario_escolar/settings.py` y agrega `'equipos'` a la lista `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        # ... otras apps de Django
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "inventario_escolar", # Esta línea puede variar si el proyecto se creó con otro nombre
        "equipos", # Añade esta línea
    ]
    ```
    La configuración de la base de datos (`DATABASES`) por defecto utiliza SQLite, lo cual es adecuado para este proyecto.

4.  **Ejecutar Migraciones:**
    Aplica las migraciones iniciales y las de tu aplicación:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crear Superusuario:**
    Para acceder al panel de administración de Django, crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico (opcional) y contraseña.

## Modelo `Equipo`

La aplicación `equipos` define un modelo `Equipo` con los siguientes campos:

*   `nombre` (CharField): Nombre del equipo (ej. "Proyector X1").
*   `categoria` (CharField): Categoría del equipo (ej. "Proyector", "Notebook", "Impresora").
*   `estado` (CharField): Estado actual del equipo (ej. "Operativo", "En reparación", "Dado de baja").
*   `fecha_ingreso` (DateField): Fecha en que el equipo fue ingresado al inventario.
*   `ubicacion` (CharField): Ubicación física del equipo (ej. "Sala 201", "Laboratorio 3").

## Administración de Equipos

1.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

2.  **Acceder al panel de administración:**
    Abre tu navegador web y visita: `http://127.0.0.1:8000/admin/`

3.  **Iniciar sesión:**
    Utiliza las credenciales del superusuario que creaste.

4.  **Gestionar equipos:**
    En el panel de administración, podrás ver la sección "Equipos" (si registraste el modelo correctamente en `equipos/admin.py`). Desde allí, puedes agregar nuevos equipos, editar los existentes y eliminarlos.

## Estructura del Proyecto

```
inventario_escolar/
├── manage.py
├── inventario_escolar/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── equipos/
    ├── __init__.py
    ├── admin.py       # Configuración del panel de administración
    ├── apps.py
    ├── models.py      # Definición del modelo Equipo
    ├── tests.py
    ├── views.py
    └── migrations/    # Archivos de migración de la base de datos
        ├── __init__.py
        └── 0001_initial.py
