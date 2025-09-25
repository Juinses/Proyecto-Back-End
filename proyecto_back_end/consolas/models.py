from django.db import models

class companies(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Company"         # Nombre en singular
        verbose_name_plural = "Companies" # Nombre en plural


class consola(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="consolas/", blank=True, null=True)
    descripcion = models.TextField()
    empresa = models.ForeignKey(companies, on_delete=models.CASCADE, related_name="consolas")  # mejor nombre

    def __str__(self):
        return self.nombre
