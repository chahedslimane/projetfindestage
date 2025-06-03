from django.shortcuts import get_object_or_404, render
from datetime import datetime
from .models import Service

# Create your views here.

def services(request):
 serv = Service.objects.all()
 
 name = None
 desc = None
 pde = None
 pau = None
 cs = None

 if 'cs' in request.GET:
    cs = request.GET['cs']
    if not cs:
       cs = 'off'

 if 'searchname' in request.GET:
     name = request.GET['searchname']
     if name:
        if cs=='on':
           serv = serv.filter(nom__contains=name)
        else:
          serv = serv.filter(nom__icontains=name)

 if 'searchdesc' in request.GET:
    desc = request.GET['searchdesc']
    if desc:
        if cs=='on':
           serv = serv.filter(description__contains=desc)
        else:
           serv = serv.filter(description__icontains=desc)

 if 'searchprixde' in request.GET and 'searchprixau' in request.GET:
    pde = request.GET['searchprixde']
    pau = request.GET['searchprixau']
    if pde and pau:
       if pde.isdigit() and pau.isdigit():
           serv = serv.filter( prix__gte=pde , prix__lte=pau )

 context = {
    'services':serv
 }

 return render ( request , 'services/services.html' ,context)

def service(request, service_id):
    context ={
        'serv':get_object_or_404(Service, pk=service_id)
    }
    return render ( request , 'services/service.html', context)

def search(request):
    return render( request, 'services/search.html')