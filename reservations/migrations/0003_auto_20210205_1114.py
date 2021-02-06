# Generated by Django 2.2.5 on 2021-02-05 02:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_bookedday'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 5, 2, 14, 42, 646621, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]