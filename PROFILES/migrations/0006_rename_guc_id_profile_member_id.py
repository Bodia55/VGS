# Generated by Django 4.1.6 on 2023-03-14 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PROFILES', '0005_profile_guc_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='guc_id',
            new_name='member_id',
        ),
    ]