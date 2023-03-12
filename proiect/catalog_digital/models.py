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
    
    def __str__(self):
        return f"{self.nume_scoala}"
    
class ClaseScoala(models.Model):
    class Meta():
        verbose_name_plural = "Clase Scoala"
       
    scoala = models.ForeignKey(Scoala, on_delete=models.CASCADE) 
    nume_clasa = models.CharField(max_length=50)
    diriginte = models.CharField(max_length=20)
    promotia = models.IntegerField()
    
    def __str__(self):
        return f"{self.scoala} {self.nume_clasa}"
    
class Profesori(models.Model):
    class Meta():
        verbose_name_plural = "Profesori"
        
    nume_profesor = models.CharField(max_length=30)
    materie = models.CharField(max_length=20)
    numar_telefon_profesor = models.IntegerField()
    adresa_mail_profesor = models.EmailField()
    scoala = models.OneToOneField(Scoala, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nume_profesor} {self.materie}"
    
    
class Elevi(models.Model):
    class Meta():
        verbose_name_plural = "Elevi"
        
    nume_elev = models.CharField(max_length=30)
    numar_telefon_elev = models.IntegerField()
    adresa_mail_elev = models.EmailField()
    scoala = models.OneToOneField(Scoala, on_delete=models.CASCADE)
    clasa = models.OneToOneField(ClaseScoala, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nume_elev} {self.adresa_mail_elev}"