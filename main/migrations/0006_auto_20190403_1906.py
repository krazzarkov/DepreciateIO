# Generated by Django 2.2 on 2019-04-04 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190403_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 19, 6, 10, 645376), verbose_name='date published'),
        ),
    ]
