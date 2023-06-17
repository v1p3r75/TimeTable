from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from TimeTable.models import User
from .helpers import redirect_authenticated_user, redirect_users

# Create your views here.

@redirect_authenticated_user
def index(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request = request, email = email, password = password)

        if user is not None:

            login(request, user)

            return redirect_users(request, user, user)

        
        return render(request, 'auth/login.html', { 'title' : 'Connexion', 'errors' : ['Email ou mot de passe incorrect']})
    
    return render(request, 'auth/login.html', { 'title' : 'Connexion' })

@redirect_authenticated_user
def register(request):
    
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        if (firstname == '' or lastname == '' or email == '' or password == ''):

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
        )
                
        auth_user = authenticate(request = request, email = email, password = password)

        login(request, auth_user)

        return redirect_users(request, user, user)
            
    return render(request, 'auth/register.html', { 'title' : 'Inscription' })


@redirect_authenticated_user
def forgotPassword(request):

    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })


def logoutUser(request):

    logout(request)

    return redirect('login')