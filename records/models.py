from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(
    max_length=10,
    choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
    default='Male')  # Default value  
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

