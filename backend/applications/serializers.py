from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'candidate_name', 'candidate_email', 'job', 'applied_by', 'status', 'applied_at']
