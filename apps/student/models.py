from django.db import models


class Superpower(models.Model):
    name = models.CharField(max_length=20)
    priority = models.IntegerField()

    class Meta:
        ordering = ['priority']
