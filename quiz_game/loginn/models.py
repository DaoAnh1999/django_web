from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Question(models.Model):
    question = models.CharField(max_length=200)
    A = models.CharField(max_length=50)
    B = models.CharField(max_length=50)
    C = models.CharField(max_length=50)
    D = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)