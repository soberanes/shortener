from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

# Create your models here.
class TackkleURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(TackkleURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = TackkleURL.objects.filter(id__gte=1)
        if items != None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class TackkleURL(models.Model):
    url       = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active    = models.BooleanField(default=True)

    objects = TackkleURLManager()

    def save(self, *args, **kwargs):
        if not self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(TackkleURL, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = '-id'
    # def my_save(self):
    #     self.save()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
