# Generated by Django 2.2 on 2019-04-03 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190402_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 2, 23, 35, 9, 16711), verbose_name='date published'),
        ),
    ]
