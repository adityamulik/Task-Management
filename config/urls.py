from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from taskmanagement.routers import urlpatterns as api_urls

urlpatterns = [
    # TaskManagement Views
    path('', include('taskmanagement.urls')),  
    # API Views
    path('api/', include(api_urls)),  
    # Auth Views
    path('accounts/login', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout', auth_views.LogoutView.as_view(), name="logout"),
    # Admin View
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)