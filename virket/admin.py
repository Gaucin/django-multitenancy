from django.contrib import admin
from virket.models import Task, AppUser


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'owner', 'is_active', 'creation_date')


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'client_id')