from rest_framework import routers
from djangoRestApi.apps.api import views
from djangoRestApi.apps.api.viewsets import TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('tasks', TaskViewSet)