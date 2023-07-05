from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from TimeTable.models import User
from .helpers import redirect_authenticated_user, redirect_users
from .models import Level
from TimeTable.helpers import send_notification
import random

# Create your views here.

@redirect_authenticated_user
def index(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request = request, email = email, password = password)

        if user is not None:

            login(request, user)

            return redirect_users(request, user)

        
        return render(request, 'auth/login.html', { 'title' : 'Connexion', 'errors' : ['Email ou mot de passe incorrect']})
    
    return render(request, 'auth/login.html', { 'title' : 'Connexion' })

@redirect_authenticated_user
def register(request):
    
    if request.method == 'POST':

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        email = request.POST.get('email')
        level_id = request.POST.get('level_id')

        if (firstname == '' or lastname == '' or email == '' or password == '' or level_id == ''):

            return render(request, 'auth/register.html', {'errors': ['Vous devez remplir tous les champs.']})


        if password != password_confirmation:

            return render(request, 'auth/register.html', {'errors': ['Les mots de passe ne sont pas les mêmes.']})


        if User.objects.filter(email = email).exists():

            error = "Cet utilisateur existe déjà. Veuillez en choisir un autre email."
            return render(request, 'auth/register.html', {'errors': [error]})
                
        user = User.objects.create_user(
            email = email,
            password = password,
            firstname = firstname,
            lastname = lastname,
            level_id = level_id,
        )
                
        auth_user = authenticate(request = request, email = email, password = password)

        login(request, auth_user)

        return redirect_users(request, user)

    levels = Level.objects.all()

    return render(request, 'auth/register.html', { 'title' : 'Inscription', 'levels': levels})

@redirect_authenticated_user
def forgotPassword(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        user = User.objects.filter(email = email)

        if user:

            otp = random.randint(100000, 999999)

            user.update(otp = otp)

            user = User.objects.get(email = email)

            send_notification("Réinitialisation de mot de passe", [user.email], "mail/reset-password.html", {"otp": otp, "user": user})

            return render(request, 'auth/reset-password.html', {'title' : 'Changer de mot de passe', 'email': email})
        
        return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié', 'errors': ['Utilisateur introuvable !']})


    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })

@redirect_authenticated_user
def resetPassword(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user_verify = User.objects.filter(email = email, otp = request.POST.get('otp'))

        if user_verify:

            user = User.objects.get(email = email)
            user.set_password(password)
            user.save()

            auth_user = authenticate(request = request, email = email, password = password)

            login(request, auth_user)

            return redirect_users(request, user)

        
        return render(request, 'auth/reset-password.html', {'title' : 'Mot de passe oublié', 'email': email, 'errors': ['Code incorrect. Veillez réessayer !']})
 
    
    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })


    
def logoutUser(request):

    logout(request)

    return redirect('login')