from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username

