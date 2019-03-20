from django.views.generic import TemplateView
from rest_framework import generics
from virket.models import AppUser
from virket.serializers import AppUserSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class UserListView(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

