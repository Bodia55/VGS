# Generated by Django 4.1.6 on 2023-04-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_resource_resource_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='resource_data',
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_link',
            field=models.CharField(default=False, max_length=800),
            preserve_default=False,
        ),
    ]
