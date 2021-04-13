from rest_framework import serializers
from .models import Song, Podcast, Audiobook

class SongSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    class Meta:
        model = Song
        fields = ['id','Name', 'Duration','created']

class PodcastSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    class Meta:
        model = Podcast
        fields = ['id','Name', 'Duration','created', 'host', 'participants']

class AudiobookSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    class Meta:
        model = Audiobook
        fields = ['id','title', 'author','Narrator', 'Duration', 'created']
