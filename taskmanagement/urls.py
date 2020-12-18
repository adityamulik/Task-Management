from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


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
    path('<pk>/task/',
        views.ProjectTaskUpdateView.as_view(),
        name='project_task_update'),
    # APIs
    path('api/projects/', views.ProjectList.as_view()),
    path('api/projects/<int:pk>', views.ProjectDetails.as_view()),
    path('api/tasks/', views.TaskList.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)