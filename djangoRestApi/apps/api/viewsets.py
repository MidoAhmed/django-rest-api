from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, TaskStatus
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter


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


class TaskList(ListAPIView):
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
