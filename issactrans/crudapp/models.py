from django.db import models

class Employes(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    fonction = models.CharField(max_length=100)
    contrat = models.CharField(max_length=50, choices=[
        ("CDI", "CDI"),
        ("CDD", "CDD"),
        ("Stage", "Stage"),
        ("Alternance", "Alternance"),
    ])
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
