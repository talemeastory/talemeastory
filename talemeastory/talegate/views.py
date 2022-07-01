import random

from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from geopy.geocoders import Nominatim

from .serializers import *

from django_ip_geolocation.decorators import with_ip_geolocation
# Create your views here.


def index(request):
    template = loader.get_template('talegate/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


class StoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Story models
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        location = request.geolocation

        geo = location['geo']
        geolocator = Nominatim(user_agent="talegate")
        location2 = geolocator.reverse(f'${geo["latitude"]}, ${geo["longitude"]}')

        serializer.validated_data['location'] = geo["latitude"] + ", " + geo["longitude"]
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Story model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_random_story():
    max_pk = Story.objects.all().aggregate(max_pk=Max('id'))['max_pk']
    while True:
        random_pk = random.randint(1, max_pk)
        story = Story.objects.filter(pk=random_pk).first()
        if story:
            return story
