from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="proyectos/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    publicado = models.BooleanField(default=True)
    destacado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "proyectos"
        ordering = ["nombre"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre
