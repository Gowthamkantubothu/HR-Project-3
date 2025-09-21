from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsAdmin, IsRecruiter, IsHiringManager

# Admin can list and create jobs
class AdminOnlyView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

# Recruiter can view only their jobs
class RecruiterOnlyView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(recruiter_name=self.request.user.username)

# Hiring Manager can view all jobs
class ManagerOnlyView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsHiringManager]
