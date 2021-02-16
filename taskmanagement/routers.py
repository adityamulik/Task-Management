from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', views.Projects, 'projects')

urlpatterns = router.urls