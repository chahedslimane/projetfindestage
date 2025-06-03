from django.contrib import admin  # Importe les outils d’administration de Django
from .models import Employes   # Importe le modèle UserProfile depuis le fichier models.py de l’application

# Enregistrement du modèle UserProfile dans l’interface d’administration Django.
# Cela permet de gérer les profils utilisateurs depuis l’admin (ajouter, modifier, supprimer).
admin.site.register(Employes)