from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):

    return render(request, 'auth/login.html', { 'title' : 'Connexion' })


def register(request):

    return render(request, 'auth/register.html', { 'title' : 'Inscription' })


def forgotPassword(request):

    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })