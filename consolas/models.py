from django.db import models

class companies(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
#Unique hace referencia a que no pueden existir dos compañias con el mismo nombre.
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Company"          # Nombre en singular
        verbose_name_plural = "Companies" # Nombre en plural


class consola(models.Model):
    nombre = models.CharField(max_length=20)

    imagen = models.ImageField(upload_to="consolas/", blank=True, null=True)
#blanck = True: permite que los caracteres en la validacion de django esten vacios.
#null = True: permite que en la BDD los campos sean guardados como nulos.
    descripcion = models.TextField()
#TextField(): Al estar vacio obliga a que hayan caracteres a menos que se añadan blank=true y null=true)
    empresa = models.ForeignKey(companies, on_delete=models.CASCADE, related_name="consolas")  # mejor nombre

    def __str__(self):
        return self.nombre
    
#NO USAR BLANCK=true para CharField o TextField para evitar consultas complejas con la BDD y posibles incongruencias. ejemplo: guardar un campo " " como null.
#Dejarlo Sencillo y Facilito :) 


"""¿Qué son los models en Django?
Son el corazón de Django ORM (Object-Relational Mapping).
Permite trabajar con la base de datos usando clases y objetos, en lugar de escribir SQL directamente.
Django se encarga de traducir tus modelos a sentencias SQL para crear tablas, relaciones, insertar, actualizar, eliminar y consultar datos."""
  