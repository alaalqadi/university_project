from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    description = models.CharField(null=True, blank=True, max_length=200)
    attachment = models.FileField(null=True, blank=True)

    STATUS_OPEN = 'open'

    STATUS_DELETED = 'deleted'

    STATUS_CHOICES = (
        (STATUS_OPEN, _('open')),

        (STATUS_DELETED, _('deleted')),
    )
    status = models.CharField(null=True, blank=True, max_length=200, choices=STATUS_CHOICES)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
