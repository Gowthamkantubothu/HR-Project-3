from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('RECRUITER', 'Recruiter'),
        ('MANAGER', 'Hiring Manager'),
        ('CANDIDATE', 'Candidate'),
    )
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('recruiter', 'Recruiter'),
        ('manager', 'Hiring Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username
