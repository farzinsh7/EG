from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # is_author = models.BoolianField(default=False)
    # special_user = models.DateTimeField(default=timezone.now)

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

class AccountHits(models.Model):
    hits = models.ManyToManyField(IPAddress, blank=True, related_name="hits")