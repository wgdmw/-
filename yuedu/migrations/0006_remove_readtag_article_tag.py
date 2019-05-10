# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuedu', '0005_readtag_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readtag',
            name='article_tag',
        ),
    ]
