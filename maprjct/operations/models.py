from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)
    author=models.CharField(max_length=25)
    def __str__(self):
        return self.author


class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=25)

class std1(models.Model):
    name=models.CharField(max_length=25)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=25)
