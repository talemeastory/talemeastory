from rest_framework import serializers
from .models import *


class ExcerptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Excerpt
        exclude = ('id', )


class StorySerializer(serializers.ModelSerializer):

    excerpt_set = ExcerptSerializer(many=True)
    text = serializers.SerializerMethodField()

    @staticmethod
    def get_text(instance):
        text = ''
        for e in instance.excerpt_set.all():
            text += e.text
        return text

    class Meta:
        model = Story
        exclude = ('id', 'slug', )
