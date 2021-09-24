# Generated by Django 3.1.3 on 2021-01-14 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stashes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_stash', models.CharField(max_length=40)),
                ('amount_of_stash', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('stash_name', models.CharField(max_length=40)),
                ('amount_deposited', models.FloatField()),
            ],
        ),
    ]
