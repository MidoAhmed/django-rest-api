from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id', 'url', 'name']


class TaskSerializer(serializers.ModelSerializer):
    is_opened = serializers.BooleanField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    user_id = serializers.IntegerField()

    # user = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'created', 'is_opened', 'user_id')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['is_opened'] = instance.is_opened()
    #     return data
