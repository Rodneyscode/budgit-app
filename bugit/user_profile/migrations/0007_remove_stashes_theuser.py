# Generated by Django 3.1.3 on 2021-02-22 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20210213_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stashes',
            name='theuser',
        ),
    ]