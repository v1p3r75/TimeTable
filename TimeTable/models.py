from django.db import models

# Create your models here.

class Role(models.Model):

    label = models.TextField( max_length = 1, choices = [

        (1, 'Adminstrateur'),
        (2, 'Professeur'),
        (3, 'Etudiant'),

    ], default = 3 )

class User(models.Model):

    lastname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 30, null = True)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    create_at = models.DateTimeField(auto_now_add = True)
    
class Level(models.Model):

    label = models.CharField(max_length = 255, unique = True)


class Subject(models.Model):

    label = models.CharField(max_length = 255)
    code = models.CharField(max_length = 255, null = True)
    total_time = models.IntegerField()
    level = models.ForeignKey(Level, on_delete = models.CASCADE)


class Classroom(models.Model):

    label = models.CharField(max_length = 255)
    capacity = models.IntegerField( null = True)


class TimeTable(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete = models.CASCADE)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    start_end = models.DateTimeField()
    week = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)