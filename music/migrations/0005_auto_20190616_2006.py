# Generated by Django 2.2.2 on 2019-06-16 14:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20190616_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 16, 14, 36, 26, 130031, tzinfo=utc)),
        ),
    ]
