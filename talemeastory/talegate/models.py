from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
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
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(StoryBook, self).save(*args, **kwargs)


class Story(models.Model):

    title = models.CharField(max_length=30)
    story_book = models.ForeignKey(StoryBook, blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True, blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stories'


class Excerpt(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    text = models.CharField(max_length=128)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.author} - {Truncator(self.text).words(num=7)}'
