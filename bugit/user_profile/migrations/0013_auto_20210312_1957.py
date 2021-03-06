# Generated by Django 3.1.3 on 2021-03-13 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0012_delete_deposittable'),
    ]

    operations = [
        migrations.AddField(
            model_name='stashes',
            name='depositamount',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='stashes',
            name='discription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stashes',
            name='predictedgoaldate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stashes',
            name='amount_of_stash',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.CreateModel(
            name='DepositInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_bank', models.CharField(max_length=100)),
                ('accountnumber', models.IntegerField()),
                ('routingnumber', models.IntegerField()),
                ('paydaycycle', models.IntegerField()),
                ('theuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
