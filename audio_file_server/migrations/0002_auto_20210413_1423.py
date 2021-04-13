# Generated by Django 3.2 on 2021-04-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_file_server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='participants',
        ),
        migrations.AddField(
            model_name='podcast',
            name='host',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
