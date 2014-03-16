from django.db import models
from django.core.urlresolvers import reverse


class Task(models.Model):

    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name