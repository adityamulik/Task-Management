from django.urls import path
from .views import landing_page, ProjectList, ProjectDetails

urlpatterns = [
  path('', landing_page, name="home"),
  path('projects/', ProjectList.as_view()),
  path('projects/<int:pk>', ProjectDetails.as_view())
]