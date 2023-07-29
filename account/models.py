from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # is_author = models.BoolianField(default=False)
    # special_user = models.DateTimeField(default=timezone.now)