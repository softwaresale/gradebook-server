from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=15)
    value = models.IntegerField(default=0)
    letter = models.CharField(max_length=2)
    student = models.CharField(max_length=15)
    teacher = models.CharField(max_length=15)
