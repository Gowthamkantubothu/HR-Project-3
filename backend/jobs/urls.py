from django.urls import path
from .views import AdminOnlyView, RecruiterOnlyView, ManagerOnlyView

urlpatterns = [
    path('admin/', AdminOnlyView.as_view(), name='admin_jobs'),
    path('recruiter/', RecruiterOnlyView.as_view(), name='recruiter_jobs'),
    path('manager/', ManagerOnlyView.as_view(), name='manager_jobs'),
]
