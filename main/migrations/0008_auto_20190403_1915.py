# Generated by Django 2.2 on 2019-04-04 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190403_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 19, 15, 14, 582651), verbose_name='date published'),
        ),
    ]
