from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from services.models import Service
import re


# Create your views here.

def signin(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:

       username = request.POST['user']
       password = request.POST['pass']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           if 'rememberme' not in request.POST:
               request.session.set_expiry(0)
           auth.login(request, user)
           #messages.success(request, 'You are now logged in')
       else:  
           messages.error(request, 'Nom utilisateur ou mot de passe invalide')
            
        
       return redirect('signin')
    else:
        return render( request , 'accounts/signin.html')
    
def logout(request):
    if request.user.is_authenticated:
            auth.logout(request)
    return redirect('index')

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
    if request.user.is_authenticated and not request.user.is_anonymous:
        serv_fav = Service.objects.get(pk=service_id)
        if UserProfile.objects.filter(user=request.user,service_favorites=serv_fav).exists():
           messages.success(request, 'ce service existe déjà  dans la liste des favoris')
        else:
            userprofile = UserProfile.objects.get(user=request.user)   
            userprofile.service_favorites.add(serv_fav)
            messages.success(request, 'Le service a été mis en favoris ')
            
        
    else:
         messages.error(request, 'Vous devez vous connecté')
         
    return redirect('/services/' + str(service_id))


def show_service_favorite(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        Serv = userInfo.service_favorites.all()
        context = { 'services':Serv }
    return render(request, 'services/services.html', context)

        