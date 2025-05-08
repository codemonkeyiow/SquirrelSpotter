# from django.contrib.auth.models import User
from django.db import models


class Squirrel(models.Model):
    name = models.CharField(max_length=255)
    # spotted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    spotted_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    spotted_on = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)