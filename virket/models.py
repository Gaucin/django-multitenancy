from django.db import models
from django.contrib.auth.models import User


class AppUser(User):
    client_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.set_password(self.password)
        super(AppUser, self).save(*args, **kwargs)

