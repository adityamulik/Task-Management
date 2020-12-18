from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'duration']


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'start_date', 'end_date']