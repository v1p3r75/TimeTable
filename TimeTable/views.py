from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required( login_url = 'login')
def index(request):

    return render(request, 'timetable/admin/home.html')


@login_required( login_url = 'login')
def loadPage(request, name):

    return render(request, 'timetable/admin/' + name + '.html')