from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
]
