# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksmanager', '0008_auto_20180114_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ManyToManyField(related_name='tasks_assigned', to=settings.AUTH_USER_MODEL, verbose_name='assigned to'),
        ),
    ]