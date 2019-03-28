from rest_framework import serializers
from virket.models import AppUser, Task
from django.contrib.auth.models import User


class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'client_id')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('description', 'owner', 'is_active', 'creation_date')


class TasksByUserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = AppUser
        fields = ('username','tasks')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

