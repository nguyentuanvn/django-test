from django.db import models
from enum import Enum


class MLInstanceStatus(str, Enum):
    active = "active"
    training = "training"

class MLInstance(models.Model):
    name = models.CharField(max_length=100)
    status = models.TextField(default=MLInstanceStatus.active)