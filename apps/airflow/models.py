from uuid import uuid4

from django.db import models


# Create your models here.
class Search(models.Model):
    search_item = models.JSONField(blank=True, null=True)
    currency = models.CharField(max_length=5, verbose_name="Валюта", null=True, blank=True)
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name='uuid')


class Currency(models.Model):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=5, null=True, blank=True)
    description = models.FloatField(null=True, blank=True)