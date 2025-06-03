from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Devis


# Create your views here.
def devis(request):
    if request.method == 'POST' and 'btnenvoyer' in request.POST:
        # Get values from the form
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        objet = request.POST.get('objet')
        message = request.POST.get('message')

        # Validation
        if not all([fname, lname, email, objet, message]):
            if not fname: messages.error(request, 'Erreur sur le Nom')
            if not lname: messages.error(request, 'Erreur sur le Prenom')
            if not email: messages.error(request, 'Erreur sur email')
            if not objet: messages.error(request, 'Erreur sur objet')
            if not message: messages.error(request, 'Erreur sur le message')
        else:
            # Créer et sauvegarder le devis
            nouveau_devis = Devis(
                nom=fname,
                pernom=lname,
                email=email,
                objet=objet,
                message=message
            )
            nouveau_devis.save()
            messages.success(request, 'Votre demande de devis a été envoyée avec succès!')
            return redirect('devis')

        return render(request, 'devis/devis.html', {
            'fname': fname,
            'lname': lname,
            'email': email,
            'objet': objet,
            'message': message,
        })
    else:
        return render(request, 'devis/devis.html')
    

    
