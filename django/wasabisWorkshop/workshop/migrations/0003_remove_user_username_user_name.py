# Generated by Django 4.0.3 on 2022-03-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_spotifytoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Ollie', max_length=60, verbose_name='name'),
            preserve_default=False,
        ),
    ]
