# Generated by Django 2.2.28 on 2024-03-20 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MVapp', '0009_remove_song_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL),
        ),
    ]
