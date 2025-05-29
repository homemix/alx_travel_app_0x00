
from django.db import models


class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

