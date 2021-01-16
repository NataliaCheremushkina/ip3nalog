from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_nalog = models.PositiveIntegerField(blank=True, null=True)
