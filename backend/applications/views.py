from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsAdmin, IsRecruiter, IsHiringManager

# Admin can view all applications
class AdminApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

# Recruiter can view applications only for their jobs
class RecruiterApplicationView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        return Application.objects.filter(job__recruiter_name=self.request.user.username)

# Hiring Manager can view all applications
class ManagerApplicationView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsHiringManager]
