from django.db import models

# Create your models here.

class Estado(models.Model):   
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.estado

class Raza(models.Model):
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
         return self.raza

class Mascotas(models.Model):
    nombre_mascota = models.CharField(max_length=30)
    raza= models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1)
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to="")
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __str__(self):
         return self.nombre_mascota
    class Meta:
        verbose_name ="Mascota"
        verbose_name_plural = "Mascotas"

