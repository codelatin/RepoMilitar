from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Proyecto")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    tutor = models.CharField(max_length=100, verbose_name="Tutor")
    programa = models.CharField(max_length=150, verbose_name="Programa")
    descripcion = models.TextField(verbose_name="Descripción")
    palabras_clave = models.CharField(max_length=300, verbose_name="Palabras Clave", help_text="Separadas por comas")
    estado = models.CharField(
        max_length=50,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En Progreso'),
            ('completado', 'Completado'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendiente'
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo