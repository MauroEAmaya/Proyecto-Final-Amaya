from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nacimiento = models.CharField(max_length=100)
    

    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.nacimiento}, {self.id}"


class Dymmy(models.Model):

  nombre = models.CharField(max_length=100)