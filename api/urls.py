from django.urls import path
from .viewsets import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:id>/', TaskRetrieveUpdateDestroyAPIView.as_view())
]
