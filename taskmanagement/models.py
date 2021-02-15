import os
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Project(models.Model):
    """
    Each individual projects consisting listed
    tasks opened by individual users.
    """
    owner = models.ForeignKey(User,
                              related_name='project_created',
                              on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()
    image = models.ImageField(upload_to='project_images/', blank=True) 

    def __str__(self):
        return self.title


class Task(models.Model):
    """
    Each task opened by individual user in
    a project.
    """

    STATUS = [
        ('O', 'Open'),
        ('P', 'In-progress'),
        ('C', 'Closed'),
    ]

    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title