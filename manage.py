#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.
Este script permite ejecutar comandos de gestión de Django como:
- startproject: para crear un nuevo proyecto Django.
- startapp: para crear una nueva aplicación dentro de un proyecto.
- runserver: para iniciar el servidor de desarrollo.
- makemigrations: para crear archivos de migración basados en cambios en los modelos.
- migrate: para aplicar las migraciones a la base de datos.
- createsuperuser: para crear un usuario administrador.
"""
import os
import sys


def main():
    """Ejecuta tareas administrativas."""
    # Establece el módulo de configuración de Django a usar.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventario_escolar.settings")
    try:
        # Intenta importar y ejecutar el comando de línea de comandos de Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no se puede importar, informa al usuario sobre posibles causas.
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando de línea de comandos con los argumentos del sistema.
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Punto de entrada principal del script.
    main()
