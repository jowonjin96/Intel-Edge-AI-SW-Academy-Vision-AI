# Generated by Django 4.2.13 on 2024-05-16 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_behaviorlog_pose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='behaviorlog',
            name='pose',
        ),
    ]