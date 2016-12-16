from __future__ import unicode_literals

from django.db import models

from shortener.models import TackkleURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, tackkleInstance):
        if isinstance(tackkleInstance, TackkleURL):
            obj, created = self.get_or_create(tackkle_url=tackkleInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    tackkle_url = models.OneToOneField(TackkleURL)
    count = models.IntegerField(default=0)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i.self.count)
