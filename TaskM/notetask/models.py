from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Task(models.Model):
    STATUS_CHOICES = [
        ('Not Start Yet', 'Not Start Yet'),
        ('Doing', 'Doing'),
        ('Finish', 'Finish'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Start Yet')

    def __str__(self):
        return self.title