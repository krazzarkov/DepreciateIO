# Generated by Django 2.2 on 2019-04-04 02:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190403_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtutorial',
            name='blogtutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 19, 46, 10, 552009), verbose_name='date published'),
        ),
    ]
