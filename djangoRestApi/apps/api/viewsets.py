from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, TaskStatus
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import authentication, permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class TasksPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class TaskListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of tasks or create new
    """
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'status')
    search_fields = ('title', 'description')

    # pagination_class = TasksPagination

    #
    def get_queryset(self):
        is_opened = self.request.query_params.get('is_opened', None)
        queryset = Task.objects.all()

        if is_opened is None:
            return super().get_queryset()
        else:
            if is_opened == "true":
                return queryset.filter(status__in=[TaskStatus.INITIATED, TaskStatus.IN_PROGRESS])
            elif is_opened == "false":
                return queryset.exclude(status__in=[TaskStatus.INITIATED, TaskStatus.IN_PROGRESS])

        return queryset


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete task
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer

    # override delete
    def delete(self, request, *args, **kwargs):
        task_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('task_data_{}'.format(task_id))
        return response

    # override update
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            task = response.data
            cache.set('task_data_{}'.format(task['id']), {
                'title': task['title'],
                'description': task['description'],
                'status': task['status'],
            })
        return response
