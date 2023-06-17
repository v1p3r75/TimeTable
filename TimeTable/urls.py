from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin-dashboard"),
    path("", views.index, name="student-dashboard"),
    path("", views.index, name="teacher-dashboard"),
]