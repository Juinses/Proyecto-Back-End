from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="juegos/", blank=True, null=True)
    descripcion = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="juegos")

    def __str__(self):
        return self.nombre