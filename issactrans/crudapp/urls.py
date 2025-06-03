from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path("index1/", views.index, name="index1"),
    path('logout/', views.user_logout, name='logout'),
     
]