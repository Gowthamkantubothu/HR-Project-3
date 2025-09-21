from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView
from .job_views import AdminOnlyView, RecruiterOnlyView, ManagerOnlyView

urlpatterns = [
    # Authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Role-based examples
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),
    path('recruiter-only/', RecruiterOnlyView.as_view(), name='recruiter_only'),
    path('manager-only/', ManagerOnlyView.as_view(), name='manager_only'),
]
