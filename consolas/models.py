from django.db import models

class Company(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  pais_origen = models.CharField(max_length=100) # País de origen
  anio_salida = models.PositiveIntegerField(default=1990)
  cantidad_consolas = models.PositiveIntegerField(default=0) # Consolas lanzadas

  def __str__(self):
    return self.nombre

  class Meta:
    verbose_name = "Company"
    verbose_name_plural = "Companies"


class Consola(models.Model):
  nombre = models.CharField(max_length=50)
  imagen = models.ImageField(upload_to="consolas/", blank=True, null=True)
  descripcion = models.TextField()
  empresa = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="consolas")
  anio_salida = models.PositiveIntegerField() # Año de lanzamiento
  ventas_totales = models.PositiveIntegerField(default=0) # Unidades vendidas
  juegos_vendidos = models.PositiveIntegerField(default=0) # Juegos vendidos para esta consola

  def __str__(self):
    return self.nombre
    
#NO USAR BLANCK=true para CharField o TextField para evitar consultas complejas con la BDD y posibles incongruencias. ejemplo: guardar un campo " " como null.
#Dejarlo Sencillo y Facilito :) 


"""¿Qué son los models en Django?
Son el corazón de Django ORM (Object-Relational Mapping).
Permite trabajar con la base de datos usando clases y objetos, en lugar de escribir SQL directamente.
Django se encarga de traducir tus modelos a sentencias SQL para crear tablas, relaciones, insertar, actualizar, eliminar y consultar datos."""
  