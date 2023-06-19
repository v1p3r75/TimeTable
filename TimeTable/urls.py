from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-dashboard"),
    path("manager/teachers", views.adminTeachers, name="admin-teachers"),
]