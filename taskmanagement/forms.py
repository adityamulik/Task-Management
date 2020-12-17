from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Task


ModuleFormSet = inlineformset_factory(Project,
                                      Task,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True)