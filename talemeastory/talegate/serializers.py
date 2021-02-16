from rest_framework import serializers
from .models import *


class ExcerptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Excerpt
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):

    excerpt_set = ExcerptSerializer(many=True)

    class Meta:
        model = Story
        fields = '__all__'
