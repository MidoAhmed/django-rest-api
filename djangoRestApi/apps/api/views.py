from django.contrib.auth.models import User, Group
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework import permissions

from djangoRestApi.apps.api.models import Task
from djangoRestApi.apps.api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'