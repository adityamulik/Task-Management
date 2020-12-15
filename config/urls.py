from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('taskmanagement.urls'), name="taskmanagement"),
    path('admin/', admin.site.urls),
]
