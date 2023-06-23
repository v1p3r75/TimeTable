from django.db import models
from Auth.models import User, Level

# Create your models here.

class Subject(models.Model):

    label = models.CharField(max_length = 255)
    code = models.CharField(max_length = 255, null = True)
    total_time = models.IntegerField()
    level = models.ForeignKey(Level, on_delete = models.CASCADE)


class Classroom(models.Model):

    label = models.CharField(max_length = 255)
    capacity = models.IntegerField( null = True)
    status = models.BooleanField( default = True)
    description = models.TextField(max_length = 255, null = True)


class TimeTable(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete = models.CASCADE)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # week = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)