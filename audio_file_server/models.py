from django.db import models
from django_mysql.models import ListCharField
# Create your models here.

class Song(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

class Podcast(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = ListCharField(base_field=models.CharField(max_length=100) ,size=10 ,max_length=(10 * 101), blank=True)


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
