# Generated by Django 2.2.2 on 2019-06-19 13:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20190619_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 13, 39, 54, 196930, tzinfo=utc)),
        ),
    ]
