# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-28 07:50
from __future__ import unicode_literals

from django.db import migrations


def tidy_progress_range(apps, schema_editor):
    """
    Tidies progress ranges because a bug had caused them to go out of range
    """
    ContentSessionLog = apps.get_model('logger', 'ContentSessionLog')
    ContentSummaryLog = apps.get_model('logger', 'ContentSummaryLog')

    # Not knowing how floating points will behave in the local database,
    # 1.0 might become bigger than 1.0!!
    ContentSessionLog.objects.filter(progress__lt=0).update(progress=0.0)
    ContentSessionLog.objects.filter(progress__gt=1).update(progress=1.0)
    ContentSummaryLog.objects.filter(progress__lt=0).update(progress=0.0)
    ContentSummaryLog.objects.filter(progress__gt=1).update(progress=1.0)


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20170531_1140'),
    ]

    operations = [
        migrations.RunPython(tidy_progress_range),
    ]
