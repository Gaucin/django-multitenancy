from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from virket.models import AppUser, Task
from virket.serializers import AppUserSerializer, UserSerializer, TasksByUserSerializer, TaskSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class UserListView(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskByUserListView(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = TasksByUserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        appUsers = AppUser.objects.all()
        serializer = AppUserSerializer(appUsers, many=True)
        response = {"status": status.HTTP_200_OK, "message": "Sucessful", "data": serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": status.HTTP_201_CREATED, "message": "Sucessful", "data": serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        response = {"status": status.HTTP_400_BAD_REQUEST, "message": "Error", "data": serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }

