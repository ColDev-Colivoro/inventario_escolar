from django.db import models

class Equipo(models.Model):
    """
    Representa un equipo tecnológico en el inventario escolar.
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre del equipo")
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    estado = models.CharField(max_length=100, verbose_name="Estado actual")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación")

    def __str__(self):
        """
        Retorna el nombre del equipo como representación en cadena.
        """
        return self.nombre
