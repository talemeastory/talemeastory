from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from datetime import datetime
from django.utils.text import slugify


# Create your models here.

class Story(models.Model):
    
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    lock_time = models.DateTimeField(null=True, blank=True)
    active_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    anonymous_name = models.CharField(max_length=48, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stories'


class Excerpt(models.Model):

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    anonymous_name = models.CharField(max_length=48, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.author} - {Truncator(self.text).words(num=7)}'
