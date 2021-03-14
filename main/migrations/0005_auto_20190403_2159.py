# Generated by Django 2.0.2 on 2019-04-03 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190403_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyval',
            old_name='key',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='keyval',
            old_name='value',
            new_name='year',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 21, 59, 43, 308973), verbose_name='date published'),
        ),
    ]