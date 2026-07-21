from django.db import models

# Create your models here.
class Educacion(models.Model):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Educacion"
        verbose_name_plural = "Educaciones"
        db_table = "educacion"

    def __str__(self):
        return self.titulo