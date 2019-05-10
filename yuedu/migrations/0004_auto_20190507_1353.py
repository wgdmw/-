# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuedu', '0003_auto_20190507_1228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='ReadComment',
        ),
        migrations.AlterModelOptions(
            name='readcomment',
            options={'verbose_name_plural': '评论', 'verbose_name': '评论'},
        ),
        migrations.AlterModelTable(
            name='readcomment',
            table='comment',
        ),
    ]
