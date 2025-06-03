from django.urls import path
from . import views

urlpatterns = [
    path('devis', views.devis, name='devis'),
]
