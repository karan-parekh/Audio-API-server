# Generated by Django 3.1.7 on 2021-03-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210326_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
