from django.urls import path
from .views import AdminApplicationView, RecruiterApplicationView, ManagerApplicationView

urlpatterns = [
    path('admin/', AdminApplicationView.as_view(), name='admin_applications'),
    path('recruiter/', RecruiterApplicationView.as_view(), name='recruiter_applications'),
    path('manager/', ManagerApplicationView.as_view(), name='manager_applications'),
]
