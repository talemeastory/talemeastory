from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify


# Create your models here.

class StoryBook(models.Model):
    """The story model is a collection of children passages...which ultimately
    make up the story :D
    """
    title = models.CharField('Story Title', max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(StoryBook, self).save(*args, **kwargs)


class Story(models.Model):

    title = models.CharField(max_length=30)
    storyBook = models.ForeignKey(StoryBook, blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True, blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)
