from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Ecorregion(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class RegistroBiologico(models.Model):
    especie = models.CharField(max_length=30)
    familia = models.CharField(max_length=30)
    nombre_comun = models.CharField(max_length=30)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    base_registro = models.TextField(max_length=40)
    identificador = models.CharField(max_length=40)
    anio_identificacion = models.IntegerField()
    departamento = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    latitud = models.FloatField()
    longitud = models.FloatField()
    autor = models.CharField(max_length=40)
    fecha_captura = models.DateField()
    ecorregion = models.ForeignKey(Ecorregion, on_delete=models.CASCADE)

    def __str__(self):
        return self.especie
    

    




