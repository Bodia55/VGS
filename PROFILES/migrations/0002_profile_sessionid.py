# Generated by Django 4.1.6 on 2023-03-12 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PROFILES', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sessionId',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True),
        ),
    ]