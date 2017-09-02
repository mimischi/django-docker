from django.db import models


class Visits(models.Model):
    """Small model to store a counter for the number of visits."""
    count = models.IntegerField(default=0)
