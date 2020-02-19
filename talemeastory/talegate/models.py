from django.db import models
from datetime import datetime
from django.utils.text import slugify


# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)
    owner = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)


