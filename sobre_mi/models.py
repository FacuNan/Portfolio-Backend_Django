from django.db import models

# Create your models here.
class SobreMi(models.Model):
        nombre = models.CharField(max_length=100)
        descripcion = models.TextField()
        fecha_nacimiento = models.DateField()
        email = models.EmailField()
        telefono = models.CharField(max_length=20)
        direccion = models.CharField(max_length=200)

        class Meta:
            verbose_name = "Sobre Mi"
            verbose_name_plural = "Sobre Mi"
            db_table = "sobre_mi"
            
        def __str__(self):
            return self.nombre