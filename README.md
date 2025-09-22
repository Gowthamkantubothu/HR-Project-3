# HR-Project-3 Advanced Role-Based Access Control (RBAC)

📌 Project Overview

The  Advanced Role-Based Access Control (RBAC)  is a web application that allows Admins/Recruiters/Managers to post jobs and Candidates to apply for jobs. The system is built using:

  Backend: Django REST Framework (DRF)
  
  Database: MySQL
  
  Authentication: JWT (JSON Web Token) using djangorestframework-simplejwt
  
  Frontend: React (to be added later)
  
This README contains the steps we followed to set up and build the project so far.


# 🛠️ Tech Stack

  Python 3.11+
  
  Django 5+
  
  Django REST Framework
  
  djangorestframework-simplejwt (JWT authentication)
  
  MySQL


# 🚀 Setup Instructions

1️⃣ Create Project Directory

    mkdir HR-Project-3
    cd HR-Project-3

2️⃣ Setup Virtual Environment

    python -m venv env
    env\Scripts\activate

3️⃣ Install Dependencies

    pip install django djangorestframework djangorestframework-simplejwt mysqlclient

4️⃣ Create Django Project & Apps

    django-admin startproject backend .
    cd backend
    python manage.py startapp accounts
    python manage.py startapp jobs
    python manage.py startapp applications


# ⚙️ Core Project Configuration

core/urls.py

Added JWT endpoints and included app routes:

    from django.contrib import admin
    from django.urls import path, include
    from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
    from django.http import JsonResponse
    
    def api_root(request):
        return JsonResponse({
            "message": "Welcome to Job Portal API",
            "available_endpoints": [
                "/api/token/ (POST) - Get JWT token",
                "/api/token/refresh/ (POST) - Refresh JWT token",
                "/api/accounts/ - User management",
                "/api/jobs/ - Job listings",
                "/api/applications/ - Job applications"
            ]
        })
    
    urlpatterns = [
        path("", api_root),
        path("admin/", admin.site.urls),
        path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path("api/accounts/", include("accounts.urls")),
        path("api/jobs/", include("jobs.urls")),
        path("api/applications/", include("applications.urls")),
    ]

# 👤 Accounts App

accounts/models.py

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
            ('candidate', 'Candidate'),
        ]
        role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
        def __str__(self):
            return self.username


# 💼 Jobs App

We added a Job model with created_by field (linked to User).

👉 While running migrations, Django asked for a default for created_by.
We provided a one-off default (e.g., user ID = 1).


# 📂 Database Migrations

Run migrations step by step:

    python manage.py makemigrations accounts jobs

👉 Prompt appeared:

    It is impossible to add a non-nullable field 'created_by'...

We selected Option 1 → entered 1 as default.

Then applied migrations:

    python manage.py migrate

# 🔑 JWT Authentication

  Endpoints available:
  
  ->POST /api/token/ → Get JWT token (username + password required)
  
  ->POST /api/token/refresh/ → Refresh JWT token



✅ Current Progress

   Project created with accounts, jobs, and applications apps
  
   Configured JWT authentication
  
   Custom User model with roles
  
   Added Job model with created_by field
  
   Database migrations applied


# 📌 Next Steps

  Implement serializers & views for Accounts, Jobs, and Applications
  
  Add permissions (Admin/Recruiter/Manager can post jobs, Candidates can apply)
  
  Connect React frontend with these APIs

# ▶️ Running the Project

    env\Scripts\activate
    cd backend
    python manage.py runserver

The API will be available at:
👉 http://127.0.0.1:8000/
