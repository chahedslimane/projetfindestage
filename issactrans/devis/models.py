from django.db import models

# Create your models here.
class Devis(models.Model):
    nom = models.CharField(max_length=255)
    pernom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    objet = models.CharField(max_length=255)
    message = models.TextField()
   
    def __str__(self):
        return self.nom

