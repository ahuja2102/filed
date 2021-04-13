"""filed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from audio_file_server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Song', views.SongList.as_view()),
    path('api/Podcast', views.PodcastList.as_view()),
    path('api/Audiobook', views.AudiobookList.as_view()),
    path('api/Song/<int:pk>', views.SongRetreiveUpdateDestroy.as_view()),
    path('api/Podcast/<int:pk>',views.PodcastRetreiveUpdateDestroy.as_view()),
    path('api/Audiobook/<int:pk>',views.AudiobookRetreiveUpdateDestroy.as_view()),
]