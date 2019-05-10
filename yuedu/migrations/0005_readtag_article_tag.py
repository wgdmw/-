# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuedu', '0004_auto_20190507_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='readtag',
            name='article_tag',
            field=models.ManyToManyField(verbose_name='文章标签', to='yuedu.Article'),
        ),
    ]
