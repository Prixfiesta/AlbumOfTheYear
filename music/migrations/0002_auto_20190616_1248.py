# Generated by Django 2.2.2 on 2019-06-16 07:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 16, 7, 18, 6, 974769, tzinfo=utc)),
        ),
    ]
