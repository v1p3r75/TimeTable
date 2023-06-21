from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Auth.models import User, Level
import html

# Create your views here.
@login_required( login_url = 'login')
def adminDashboard(request):

    return render(request, 'timetable/admin/home.html')


@login_required( login_url = 'login')
def adminDash(request):

    return render(request, 'timetable/admin/dash.html')

@login_required( login_url = 'login')
def userAccount(request):

    if request.method == 'POST':

        if request.POST.get('action') == 'edit':

            if request.POST.get('action-detail') == 'info':

                data = {
                    'id': request.POST.get('id'),
                    'lastname': request.POST.get('lastname'),
                    'firstname': request.POST.get('firstname'),
                    'phone': request.POST.get('phone'),
                    'email': request.POST.get('email'),
                    'level_id': request.POST.get('level_id'),
                }
                
                if User.objects.get(id = data.get('id')):
                                    
                    User.objects.filter(id = data.get('id')).update(**data)

                    return JsonResponse({'success': True, 'message': 'Mise à jour avec succès', 'data': data})
                
                return JsonResponse({'success': False, 'message': 'L\'élément est introuvable.'})

            if request.POST.get('action-detail') == 'password':

                data = {
                    'id': request.POST.get('id'),
                    'new_password': request.POST.get('new_password'),
                    'password': request.POST.get('password'),
                    'password_confirmation': request.POST.get('password_confirmation'),
                }
                
                if (data.get('new_password') != data.get('password_confirmation')):
                    
                    return JsonResponse({'success': False, 'message': 'Confirmation de mot passe échoué.'})

                user = User.objects.get(id = data.get('id'))

                if user:
                        if user.check_password(data.get('password')):

                            user.set_password(data.get('new_password'))
                            user.save()
                            return JsonResponse({'success': True, 'message': 'Mise à jour avec succès', 'data': data})

                        return JsonResponse({'success': False, 'message': 'Mot de passe incorrect.'})
                
                return JsonResponse({'success': False, 'message': 'L\'élément est introuvable.'})



        if request.POST.get('action') == 'del':

            if User.objects.get(id = request.POST.get('id')):
                                
                User.objects.filter(id = request.POST.get('id')).delete()

                return JsonResponse({'success': True, 'message': 'Supprimer avec succès'})
            
            return JsonResponse({'success': False, 'message': 'L\'élément est introuvable.'})
        

    levels = Level.objects.all()

    tabs = []

    for level in levels:
        tabs.append({"id": level.id, "level": level.label})

    return render(request, 'timetable/account.html', {'levels': levels})


@login_required( login_url = 'login')
def adminTeachers(request):

    if request.method == 'POST':

        if request.POST.get('action') == 'add':

            
            data = {
                'lastname': request.POST.get('lastname'),
                'firstname': request.POST.get('firstname'),
                'phone': request.POST.get('phone'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
                'role_id': 2,
            }

            if User.objects.filter(email = data.get('email')).exists():
                
                return JsonResponse({'success': False, 'message': 'L\'adresse email existe déjà.'})
                
            record = User.objects.create(**data)

            return JsonResponse({'success': True, 'message': 'Ajouter avec succès', 'data': data})
        
        
        if request.POST.get('action') == 'edit':

            
            data = {
                'id': request.POST.get('id'),
                'lastname': request.POST.get('lastname'),
                'firstname': request.POST.get('firstname'),
                'phone': request.POST.get('phone'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
            }

            if User.objects.get(id = data.get('id')):
                                
                User.objects.filter(id = data.get('id')).update(**data)

                return JsonResponse({'success': True, 'message': 'Mise à jour avec succès', 'data': data})
            
            return JsonResponse({'success': False, 'message': 'L\'élément est introuvable.'})
        

        if request.POST.get('action') == 'del':

            if User.objects.get(id = request.POST.get('id')):
                                
                User.objects.filter(id = request.POST.get('id')).delete()

                return JsonResponse({'success': True, 'message': 'Supprimer avec succès'})
            
            return JsonResponse({'success': False, 'message': 'L\'élément est introuvable.'})
        


    users = User.objects.filter(role_id = 2).all()

    tabs = []

    for user in users:
        tabs.append({"id": user.id, "lastname": user.lastname, "firstname": user.firstname, "email": user.email, "phone": user.phone, "password": user.password})

    return render(request, 'timetable/admin/teachers.html', {'users': html.unescape(tabs)})