from django.db import models
from jobs.models import Job
from accounts.models import User

class Application(models.Model):
    candidate_name = models.CharField(max_length=100)
    candidate_email = models.EmailField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Who submitted this application
    status = models.CharField(max_length=20, default='Pending')  # Pending, Accepted, Rejected
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} - {self.job.title}"
