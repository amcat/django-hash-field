from django.db import models
from django_hash_field import HashField

class HashTest(models.Model):
    hash_field = HashField()
    i = models.IntegerField()

