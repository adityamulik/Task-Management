from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'start_date', 'end_date']