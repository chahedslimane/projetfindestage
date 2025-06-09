"""
URL configuration for issactrans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header='ISSACTRANSPORT'
admin.site.site_title='PORTAIL MULTI SOCIETE ISSAC TRANSPORTT'
admin.site.index_title='BIENVENUE SUR ADMINITRATEUR ISSAC TRANSPORT'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path("devis/", include("devis.urls")),
    path('accounts/' , include('accounts.urls')),
    path('services/', include('services.urls') ),
    path("crudapp/", include("crudapp.urls")),
    path('schema-viewer/', include('schema_viewer.urls')),
    path("data-browser/", include("data_browser.urls"))


    

      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


