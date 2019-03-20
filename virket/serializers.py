from rest_framework import serializers
from virket.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'client_id')

