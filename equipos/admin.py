from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Equipo.
    Define cómo se mostrarán y gestionarán los equipos en el admin de Django.
    """
    # Campos que se mostrarán en la lista de equipos en el panel de administración.
    list_display = ('nombre', 'categoria', 'estado', 'fecha_ingreso', 'ubicacion')
    # Campos por los cuales se podrá filtrar la lista de equipos.
    list_filter = ('categoria', 'estado', 'ubicacion')
    # Campos por los cuales se podrá buscar dentro de la lista de equipos.
    search_fields = ('nombre', 'categoria', 'ubicacion')
