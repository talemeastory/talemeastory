from rest_framework import serializers
from .models import *


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'


class ExcerptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Excerpt
        fields = '__all__'