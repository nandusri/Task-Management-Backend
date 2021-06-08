from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet, basename='projects'),
router.register(r'tasks', views.TaskViewSet, basename='tasks'),

urlpatterns = router.urls