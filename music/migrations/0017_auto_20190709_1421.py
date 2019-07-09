# Generated by Django 2.2.2 on 2019-07-09 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20190709_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, upload_to='album-image'),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, upload_to='artist-image'),
        ),
        migrations.AlterField(
            model_name='album',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 8, 51, 51, 824800, tzinfo=utc)),
        ),
    ]