# Generated by Django 2.2.5 on 2021-01-06 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversation', to=settings.AUTH_USER_MODEL),
        ),
    ]
