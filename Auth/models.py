from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("L'adresse e-mail est requise.")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('role_id', 1)
        return self.create_user(email, password, **extra_fields)

class Role(models.Model):

    label = models.TextField( max_length = 1, choices = [

        (1, 'Adminstrateur'),
        (2, 'Professeur'),
        (3, 'Etudiant'),

    ], default = 3 )
 

class User(AbstractBaseUser):

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    username = models.CharField( max_length = 50, null = True, unique = True)
    lastname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 30, null = True)
    role = models.ForeignKey(Role, on_delete = models.CASCADE, default = 3)
    create_at = models.DateTimeField(auto_now_add = True)
   