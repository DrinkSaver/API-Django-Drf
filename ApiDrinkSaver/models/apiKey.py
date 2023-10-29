import uuid
from django.db import models
from django.contrib.auth.models import User


class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.key)
