import random

from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .serializers import *
# Create your views here.


def index(request):
    return HttpResponse('Hello, This is Edwin and Sergios multimillion dollar idea <3')


class StoryViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    ViewSet for the Story model
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    @action(methods=['get'], detail=False,
            url_path='shuffle', url_name='shuffle')
    def shuffle_story(self, request):
        story = get_random_story()
        story = StorySerializer(story).data
        return Response(story)


class ExcerptViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Excerpt model
    """
    queryset = Excerpt.objects.all()
    serializer_class = ExcerptSerializer


def get_random_story():
    max_pk = Story.objects.all().aggregate(max_pk=Max('id'))['max_pk']
    while True:
        random_pk = random.randint(1, max_pk)
        story = Story.objects.filter(pk=random_pk).first()
        if story:
            return story
