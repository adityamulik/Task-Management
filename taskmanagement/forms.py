from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date']
