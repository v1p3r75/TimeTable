from django.urls import path
from . import views

urlpatterns = [
    path("login", views.index, name="index"),
    path("register", views.register, name="index"),
    path("forgot-password", views.forgotPassword, name="index"),
]