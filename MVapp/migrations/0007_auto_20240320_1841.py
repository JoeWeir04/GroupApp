# Generated by Django 2.2.28 on 2024-03-20 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MVapp', '0006_song_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL),
        ),
    ]