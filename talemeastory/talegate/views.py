from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, mixins

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


class ExcerptViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Excerpt model
    """
    queryset = Excerpt.objects.all()
    serializer_class = ExcerptSerializer
