# Generated by Django 3.2 on 2021-04-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_file_server', '0002_auto_20210413_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='host',
            field=models.CharField(max_length=100),
        ),
    ]
