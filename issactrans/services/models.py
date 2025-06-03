from django.db import models
from datetime import datetime

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6 , decimal_places=2)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField( default=datetime.now)

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['-publish_date']