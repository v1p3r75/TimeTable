from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

def index(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email = email, password = password)

        if user is not None:

            print('Connected')
            return 0
        
        print('Not Connected')
    
    return render(request, 'auth/login.html', { 'title' : 'Connexion' })


def register(request):

    return render(request, 'auth/register.html', { 'title' : 'Inscription' })


def forgotPassword(request):

    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })