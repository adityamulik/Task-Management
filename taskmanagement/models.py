import os
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


class Base(models.Model):
    """
    Base Abstract Class created with common fields
    in both Project & Task Models.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    due_date = models.DateField()

    class Meta:
        abstract = True

    def clean(self, *args, **kwargs):
        if self.due_date < self.start_date:
            raise ValidationError("Date cannot be smaller than start date.")
        else:
            super().save(*args, **kwargs)


class Project(Base):
    """
    Each individual projects consisting listed
    tasks opened by individual users.
    """    

    STATUS = [
        ('A', 'Active'),
        ('IA' ,'Inactive'),
    ]

    project_id = models.AutoField(primary_key=True,)
    owner = models.ForeignKey(User,
                              related_name='project_created',
                              on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=STATUS)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.title


class Task(Base):
    """
    Each task opened by individual user in
    a project.
    """

    STATUS = [
        ('O', 'Open'),
        ('P', 'In-progress'),
        ('C', 'Closed'),
    ]

    LABEL = [
        ('H', 'High Priority'),
        ('L', 'Low Priority'),
        ('M', 'Medium Priority'),
    ]

    task_id = models.AutoField(primary_key=True)
    assignee = models.ForeignKey(User,
                              related_name='task_created',
                              on_delete=models.PROTECT)
    project = models.ForeignKey(Project, 
                                related_name="tasks", 
                                on_delete=models.CASCADE, 
                                verbose_name="Project Associated: ")  
    status = models.CharField(max_length=2, choices=STATUS)
    labels = models.CharField(max_length=10, choices=LABEL)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return self.title


class Workflow(models.Model):
    pass