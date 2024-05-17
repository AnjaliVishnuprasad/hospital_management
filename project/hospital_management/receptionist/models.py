from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PatientRegistration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    op_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    # Additional fields can be added as per your requirements

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Consultation_details(models.Model):
    op_number = models.BigIntegerField(unique=False)
    patient_name = models.CharField(max_length=100)
    date=models.DateField()
    doctor=models.CharField(max_length=100)
    symptoms=models.TextField(null=True)
    Diagnosis=models.TextField(null=True)
    prescription=models.TextField(null=True)
    is_consulted=models.BooleanField(default=False)
    bill_amount=models.BigIntegerField(blank=True, null=True)


    def __str__(self):
        return f"OP Number: {self.op_number}, Date: {self.date}"