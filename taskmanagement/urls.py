from django.urls import path
from .views import HomePage, ProjectList, ProjectDetails

urlpatterns = [
  path('', HomePage.as_view(), name="home"),
  # path('project/<int:pk>', project, name="project"),
  # path('task/<int:pk', task, name="task"),

  # APIs
  path('api/projects/', ProjectList.as_view()),
  path('api/projects/<int:pk>', ProjectDetails.as_view())
]