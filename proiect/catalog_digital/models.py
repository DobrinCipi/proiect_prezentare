from django.db import models

# Create your models here.
class Scoala(models.Model):
    
    class Meta():
        verbose_name_plural= "Scoli"
        
    nume_scoala = models.CharField(unique=True, max_length= 33)
    nume_director = models.CharField(max_length=20)
    adresa_scoala = models.CharField(unique=True, max_length=50)
    oras = models.CharField(max_length=30)
    judet = models.CharField(max_length=50)
    
class ClaseScoala(models.Model):
    class Meta():
        verbose_name_plural = "Clase Scoala"
       
    scoala = models.ForeignKey(Scoala, on_delete=models.CASCADE) 
    nume_clasa = models.CharField(max_length=20)
    diriginte = models.CharField(max_length=20)
    promotia = models.IntegerField()