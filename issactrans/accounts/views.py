from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from services.models import Service
import re


# Create your views here.

def signin(request):
    """
    Gère le processus de connexion des utilisateurs.
    Flux :
    1. Affichage du formulaire de connexion (GET)
    2. Vérification des identifiants (POST)
    3. Authentification et création de session
    """
    # Étape 1: Vérification si la requête est de type POST (soumission du formulaire)
    if request.method == 'POST' and 'btnlogin' in request.POST:
        # Étape 2: Récupération des identifiants depuis le formulaire
        username = request.POST['user']
        password = request.POST['pass']

        # Étape 3: Vérification des identifiants avec l'authentification Django
        # Cette étape correspond à la vérification dans la base de données
        user = auth.authenticate(username=username, password=password)

        # Étape 4: Si l'utilisateur existe et est valide
        if user is not None:
            # Étape 5: Gestion de l'option "Se souvenir de moi"
            # Si la case n'est pas cochée, la session expire à la fermeture du navigateur
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
                
            # Étape 6: Connexion de l'utilisateur (création de la session)
            auth.login(request, user)
            
            # Message de succès (optionnel)
            #messages.success(request, 'Connexion réussie !')
            
            # Redirection vers la page d'accueil après connexion
            return redirect('index')
        else:  
            # Étape 4a: Message d'erreur si les identifiants sont invalides
            messages.error(request, 'Nom utilisateur ou mot de passe invalide')
            
        return redirect('signin')
    else:
        # Étape 1a: Affichage du formulaire de connexion pour les requêtes GET
        return render(request, 'accounts/signin.html')
def signup(request):
    """
    Gère le processus d'inscription des utilisateurs.
    Flux :
    1. Affichage du formulaire d'inscription (GET)
    2. Validation des données du formulaire (POST)
    3. Vérification de l'unicité de l'email
    4. Création du compte utilisateur
    """
    # Étape 1: Vérification si la requête est de type POST (soumission du formulaire)
    if request.method == 'POST' and 'btnsignup' in request.POST:
        # Récupération des données du formulaire
        fname = request.POST.get('fname', '').strip()
        lname = request.POST.get('lname', '').strip()
        email = request.POST.get('email', '').strip().lower()
        username = request.POST.get('user', '').strip()
        password = request.POST.get('pass', '').strip()
        
        # Étape 2: Validation des champs obligatoires
        if not all([fname, lname, email, username, password]):
            messages.error(request, 'Tous les champs sont obligatoires')
            return render(request, 'accounts/signup.html', {
                'fname': fname,
                'lname': lname,
                'email': email,
                'user': username
            })
        
        # Étape 3: Vérification du format de l'email
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, 'Format d\'email invalide')
            return render(request, 'accounts/signup.html', {
                'fname': fname,
                'lname': lname,
                'email': email,
                'user': username
            })
        
        # Étape 4: Vérification de l'unicité de l'email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé')
            return render(request, 'accounts/signup.html', {
                'fname': fname,
                'lname': lname,
                'user': username
            })
        
        # Étape 5: Vérification de l'unicité du nom d'utilisateur
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris')
            return render(request, 'accounts/signup.html', {
                'fname': fname,
                'lname': lname,
                'email': email
            })
        
        # Étape 6: Création du compte utilisateur
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=fname,
                last_name=lname
            )
            
            # Connexion automatique après inscription
            auth.login(request, user)
            messages.success(request, 'Inscription réussie ! Vous êtes maintenant connecté.')
            return redirect('index')
            
        except Exception as e:
            messages.error(request, f'Une erreur est survenue lors de la création du compte: {str(e)}')
            return render(request, 'accounts/signup.html', {
                'fname': fname,
                'lname': lname,
                'email': email,
                'user': username
            })
    
    # Affichage du formulaire d'inscription (GET)
    return render(request, 'accounts/signup.html')    
def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
       
       #variables for fields
        fname = None
        lname = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None

        #Get values from the form
        if 'fname' in request.POST: fname = request.POST['fname']
        else: messages.error(request, 'Erreur sur  first name')

        if 'lname' in request.POST: lname = request.POST['lname']
        else: messages.error(request, 'Erreur sur  last name')

        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request, 'Erreur sur  address')

        if 'address2' in request.POST: address2 = request.POST['address2']
        else: messages.error(request, 'Erreur sur le address2')

        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request, 'Erreur sur city')

        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request, 'Erreur sur state')

        if 'zip' in request.POST: zip_number = request.POST['zip']
        else: messages.error(request, 'Erreur sur le zip')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request, 'Erreur sur email')

        if 'user' in request.POST: username = request.POST['user']
        else: messages.error(request, 'Erreur sur username')

        if 'pass' in request.POST: password = request.POST['pass']
        else: messages.error(request, 'Erreur sur le password')

        if 'terms' in request.POST: terms = request.POST['terms']
        
         #Check the values
        if fname and lname and address and address2 and city and state and zip_number and email and username and password:
            if terms == 'on':
                 #Vérifiez si le nom d’utilisateur est pris
                if User.objects.filter(username=username).exists():
                     messages.error(request, 'Ce username est pris')
                else:
                    #Vérifiez si l'email' est pris
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Cet email est pris')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt, email):
                             #dd user
                               user = User.objects.create_user(
                               first_name=fname, last_name=lname, email=email,
                               username=username, password=password
                               )
                               user.save()
                               # Créer le profil utilisateur
                               userprofile = UserProfile.objects.create(
                                   user=user,
                                   address=address,
                                   address2=address2,
                                   city=city,
                                   state=state,
                                   zip_number=zip_number
                               )
                               userprofile.save()
                              # clear fields
                               fname = ''
                               lname = ''
                               address = ''
                               address2 = ''
                               city = ''
                               state = '' 
                               zip_number = ''
                               email = ''
                               username = ''
                               password = ''
                               terms = None
                                                             
                              #success Message
                               messages.success(request, 'Votre compte est créé')
                               is_added = True
                        else:
                         messages.error(request, 'E-mail invalide')
            else:
                messages.error(request, 'Vous devez accepter les conditions')
        else:
            messages.error(request, 'Vérifier les champs vides')
       
        return render(request, 'accounts/signup.html',{
            'fname':fname,
            'lname':lname,
            'address':address,
            'address2':address2,
            'city':city,
            'state':state,
            'zip':zip_number,
            'email':email,
            'user':username,
            'pass':password,
            'is_added':is_added
        })
        
    else:
        return render(request, 'accounts/signup.html')
    

def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:

       if request.user is not None and request.user.id != None:
          userprofile = UserProfile.objects.get(user=request.user)

          if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['address2'] and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['email'] and request.POST['user'] and request.POST['pass']:
                 request.user.first_name = request.POST['fname']
                 request.user.last_name = request.POST['lname']
                 userprofile.address = request.POST['address']
                 userprofile.address2 = request.POST['address2']
                 userprofile.city = request.POST['city']
                 userprofile.state = request.POST['state']
                 userprofile.zip_number = request.POST['zip']
                 #request.user.email = request.POST['email']
                 #request.user.username = request.POST['user']
                 if not request.POST['pass'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['pass'])
                 request.user.save()   
                 userprofile.save()
                 auth.login(request, request.user)
                 messages.success(request, 'Vos données ont été enregistrées') 
          else:
                 messages.error(request, 'Vérifiez vos valeurs et vos données') 
       
       return redirect('profile')
    else:
        #if request.user.is_anonymous:return redirect('index')
        #if request.user.id == None:return redirect('index')
       
        if request.user is not None:

            context = None
            if not request.user.is_anonymous:
                #ou if request.user.id!=None:
                userprofile = UserProfile.objects.get(user=request.user)

                context = {
                    'fname':request.user.first_name,
                    'lname':request.user.last_name,
                    'address':userprofile.address,
                    'address2':userprofile.address2,
                    'city':userprofile.city,
                    'state':userprofile.state,
                    'zip':userprofile.zip_number,
                    'email':request.user.email,
                    'user':request.user.username,
                    'pass':request.user.password
                    }
            return render(request , 'accounts/profile.html', context)
        else:
         return redirect('profile')
     
def service_favorite(request, service_id):
    """
    Gère l'ajout d'un service aux favoris d'un utilisateur.
    Flux :
    1. Vérification de l'authentification de l'utilisateur
    2. Récupération du service concerné
    3. Vérification si le service est déjà en favori
    4. Ajout du service aux favoris si nécessaire
    5. Redirection vers la page du service avec un message approprié
    """
    # Étape 1: Vérification si l'utilisateur est connecté
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            # Étape 2: Récupération du service à partir de l'ID fourni
            serv_fav = Service.objects.get(pk=service_id)
            
            # Étape 3: Vérification si le service est déjà dans les favoris de l'utilisateur
            if UserProfile.objects.filter(user=request.user, service_favorites=serv_fav).exists():
                # Message si le service est déjà en favori
                messages.info(request, 'Ce service est déjà dans votre liste de favoris')
            else:
                # Étape 4: Ajout du service aux favoris de l'utilisateur
                userprofile = UserProfile.objects.get(user=request.user)   
                userprofile.service_favorites.add(serv_fav)
                # Message de succès
                messages.success(request, 'Le service a été ajouté à vos favoris')
                
        except Service.DoesNotExist:
            # Gestion du cas où le service n'existe pas
            messages.error(request, 'Le service demandé n\'existe pas')
        except UserProfile.DoesNotExist:
            # Gestion du cas où le profil utilisateur n'existe pas
            messages.error(request, 'Profil utilisateur introuvable')
    else:
        # Redirection vers la page de connexion avec le paramètre next pour revenir au service
        messages.warning(request, 'Veuillez vous connecter pour ajouter ce service à vos favoris')
        login_url = f'/accounts/signin?next={request.path}'
        return redirect(login_url)
     
    # Étape 5: Redirection vers la page du service
    return redirect('/services/' + str(service_id))

def show_service_favorite(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        Serv = userInfo.service_favorites.all()
        context = { 'services':Serv }
    return render(request, 'services/services.html', context)

        
def logout(request):
    if request.user.is_authenticated:
            auth.logout(request)
    return redirect('index')