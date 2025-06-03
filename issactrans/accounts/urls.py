from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup , name='signup'),
    path('profile/', views.profile, name='profile'),
    path('service_favorite/<int:service_id>', views.service_favorite, name='service_favorite'),
    path('show_service_favorite', views.show_service_favorite, name='show_service_favorite'),
]