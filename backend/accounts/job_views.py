from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdmin, IsRecruiter, IsHiringManager

# Example protected endpoints

class AdminOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin! You can see everything."})


class RecruiterOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get(self, request):
        return Response({"message": "Hello Recruiter! You can create jobs but not delete."})


class ManagerOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsHiringManager]

    def get(self, request):
        return Response({"message": "Hello Hiring Manager! You can only see assigned candidates."})
