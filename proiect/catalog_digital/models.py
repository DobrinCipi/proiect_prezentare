from django.db import models

# Create your models here.
class Scoala(models.Model):
    nume = models.CharField(unique=True, max_length= 33)
    nume_director = models.CharField
    