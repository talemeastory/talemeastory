from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', )


class ExcerptSerializer(serializers.ModelSerializer):
    text = serializers.CharField(trim_whitespace=False)
    author_instance = UserSerializer(source='author', required=False)

    class Meta:
        model = Excerpt
        exclude = ('id', )


class StorySerializer(serializers.ModelSerializer):

    active_author_instance = UserSerializer(source='active_author', required=False)
    excerpt_set = ExcerptSerializer(many=True, required=False)
    text = serializers.SerializerMethodField()

    @staticmethod
    def get_text(instance):
        text = ''
        for e in instance.excerpt_set.all():
            text += " " + e.text
        return text

    class Meta:
        model = Story
        exclude = ('slug', )
