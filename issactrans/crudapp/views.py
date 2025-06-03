from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import Employes
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index1')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, 'crudapp/login.html')



@login_required
def index(request):
    employes = Employes.objects.all()

    if request.method == "POST":
        email = request.POST.get("email")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        fonction = request.POST.get("fonction")
        contrat = request.POST.get("contrat")

        if "add" in request.POST:
            # Vérifier si l'email existe déjà
            if Employes.objects.filter(email=email).exists():
                messages.error(request, "Cet email est déjà utilisé par un autre employé.")
                return redirect("index1")

            Employes.objects.create(
                nom=nom,
                prenom=prenom,
                adresse=adresse,
                fonction=fonction,
                contrat=contrat,
                email=email,
            )
            messages.success(request, "Employé ajouté avec succès.")
            return redirect("index1")

        elif "update" in request.POST:
            employe_id = request.POST.get("id")
            employe = Employes.objects.get(id=employe_id)

            # Vérifier que l'email n'appartient pas à un autre employé
            if Employes.objects.filter(email=email).exclude(id=employe_id).exists():
                messages.error(request, "Cet email est déjà utilisé par un autre employé.")
                return redirect("index1")

            employe.nom = nom
            employe.prenom = prenom
            employe.adresse = adresse
            employe.fonction = fonction
            employe.contrat = contrat
            employe.email = email
            employe.save()
            messages.success(request, "Employé mis à jour avec succès.")
            return redirect("index1")

        elif "delete" in request.POST:
            Employes.objects.get(id=request.POST.get("id")).delete()
            messages.success(request, "Employé supprimé avec succès.")
            return redirect("index1")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            employes = Employes.objects.filter(
                Q(nom__icontains=query) |
                Q(prenom__icontains=query) |
                Q(adresse__icontains=query) |
                Q(fonction__icontains=query) |
                Q(contrat__icontains=query) |
                Q(email__icontains=query)
            )

    return render(request, "crudapp/index1.html", {"employe": employes})


def user_logout(request):
    logout(request)
    return redirect("/")
