# Generated by Django 3.1.7 on 2021-03-26 14:58

import api.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210326_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[api.validators.datetime_validator]),
        ),
    ]
