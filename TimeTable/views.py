from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required( login_url = 'login')
def adminDashboard(request):

    return render(request, 'timetable/admin/home.html')


@login_required( login_url = 'login')
def adminDash(request):

    return render(request, 'timetable/admin/dash.html')


@login_required( login_url = 'login')
def adminTeachers(request):

    return render(request, 'timetable/admin/teachers.html')