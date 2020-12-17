from django.urls import path
from . import views



urlpatterns = [
  path('', 
      views.ProjectListView.as_view(), 
      name="manage_project_list"),
  path('create', 
      views.ProjectCreateView.as_view(), 
      name="project_create"),
  path('<pk>/update', 
      views.ProjectUpdateView.as_view(), 
      name="project_update"),
  path('<pk>/delete', 
      views.ProjectDeleteView.as_view(), 
      name="project_delete"),

  # APIs
  path('api/projects/', views.ProjectList.as_view()),
  path('api/projects/<int:pk>', views.ProjectDetails.as_view())
]