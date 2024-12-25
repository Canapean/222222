from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(default=1)
    is_status = models.BooleanField(default=True)
