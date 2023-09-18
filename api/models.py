from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    cursos = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
    

    def __str__(self):
        return self.nombre