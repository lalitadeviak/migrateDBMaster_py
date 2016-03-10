from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.TextField(max_length=200)

