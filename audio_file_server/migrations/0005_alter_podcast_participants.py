# Generated by Django 3.2 on 2021-04-13 08:58

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_file_server', '0004_podcast_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=100), max_length=1010, size=10),
        ),
    ]
