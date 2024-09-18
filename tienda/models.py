from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombres = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)  # Un DNI en Perú tiene 8 dígitos
    telefono = models.CharField(max_length=9)  # Un teléfono móvil en Perú tiene 9 dígitos    
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateTimeField('fecha de nacimiento')
    fecha_de_publicacion = models.DateTimeField('fecha de publicacion')
    
    def __str__(self):
        return self.nombres 
