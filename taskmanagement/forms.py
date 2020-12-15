from django import forms
from .models import Project, Task


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'duration', 'image']


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', 'description', 'start_date', 'end_date']