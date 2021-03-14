# Generated by Django 2.2 on 2019-04-04 01:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190402_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 18, 56, 11, 599298), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(db_index=True, max_length=240)),
                ('price', models.CharField(db_index=True, max_length=240)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Phone')),
            ],
        ),
    ]
