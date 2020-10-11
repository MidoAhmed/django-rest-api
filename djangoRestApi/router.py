from rest_framework import routers
from api import views
from api.viewsets import TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('tasks', TaskViewSet)

