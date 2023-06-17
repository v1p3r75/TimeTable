from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from TimeTable.models import User

# Create your views here.

def index(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email = email, password = password)

        if user is not None:

            if (user.role.id == 1) : return redirect('admin-dashboard') 
            if (user.role.id == 2) : return redirect('teacher-dashboard') 
            else : return redirect('student-dashboard')

        
        return render(request, 'auth/login.html', { 'title' : 'Connexion', 'errors' : ['Email ou mot de passe incorrect']})
    
    return render(request, 'auth/login.html', { 'title' : 'Connexion' })


def register(request):
    
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        if (firstname != '' or lastname != '' or email != '' or password != ''):

            if password == password_confirmation:

                if User.objects.filter(email = email).exists():

                    error = "Cet utilisateur existe déjà. Veuillez en choisir un autre email."
                    return render(request, 'auth/register.html', {'errors': [error]})
                
                user = User.objects.create_user(
                    email = email,
                    password = password,
                    firstname = firstname,
                    lastname = lastname,
                )
                
                auth_user = authenticate(request, email = email, password = password)
                login(request, auth_user)

                if (user.role.id == 1) : return redirect('admin-dashboard') 
                if (user.role.id == 2) : return redirect('teacher-dashboard') 
                else : return redirect('student-dashboard')
                

            return render(request, 'auth/register.html', {'errors': ['Les mots de passe ne sont pas les mêmes.']})

        return render(request, 'auth/register.html', {'errors': ['Vous devez remplir tous les champs.']})


    return render(request, 'auth/register.html', { 'title' : 'Inscription' })


def forgotPassword(request):

    return render(request, 'auth/forgot-password.html', {'title' : 'Mot de passe oublié' })