from django.db import models
from django.contrib.auth.models import User


class AppUser(User):
    client_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.set_password(self.password)
        super(AppUser, self).save(*args, **kwargs)


class Task(models.Model):
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

