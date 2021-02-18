from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    status_display = serializers.CharField(
        source='get_status_display'
    )

    owner = serializers.CharField(source='owner.username')

    class Meta:
        model = Project
        exclude = ["status"]


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'start_date', 'end_date']