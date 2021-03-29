from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ExcerptSerializer(serializers.ModelSerializer):

    author_instance = UserSerializer(source='author', required=False)

    class Meta:
        model = Excerpt
        exclude = ('id', )


class StorySerializer(serializers.ModelSerializer):

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
