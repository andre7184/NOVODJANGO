from django.db import models
from django.contrib.auth.models import AbstractUser

class CustonUser(AbstractUser):
    is_aluno = models.BooleanField(default=False)
