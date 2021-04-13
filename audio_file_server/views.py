from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Song, Podcast, Audiobook
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from django.http import JsonResponse


# Create your views here.
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except:
            raise ValidationError('Negative values in Duration Not Allowed')

class PodcastList(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except:
            raise ValidationError('Negative values in Duration Not Allowed')

class AudiobookList(generics.ListCreateAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except:
            raise ValidationError('Negative values in Duration Not Allowed')

class SongRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(id=self.kwargs['pk'])

class PodcastRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PodcastSerializer

    def get_queryset(self):
        return Podcast.objects.filter(id=self.kwargs['pk'])

class AudiobookRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AudiobookSerializer

    def get_queryset(self):
        return Audiobook.objects.filter(id=self.kwargs['pk'])
