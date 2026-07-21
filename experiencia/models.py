from django.db import models

# Create your models here.
class Experiencia(models.Model):
    empresa= models.CharField(max_length=100)
    puesto= models.CharField(max_length=100)
    fecha_inicio= models.DateField()
    fecha_fin= models.DateField(null=True, blank=True)
    descripcion= models.TextField()

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        db_table = "experiencias"

    def __str__(self):
        return self.puesto