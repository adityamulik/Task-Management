from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.Serializer):
    
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'description', 'duration', 'image']



