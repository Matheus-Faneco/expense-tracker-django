from django.db import models
from django.contrib.auth.models import AbstractUser

#User padrão Django
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username




