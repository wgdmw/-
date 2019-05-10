# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuedu', '0002_auto_20190506_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('comment', models.CharField(max_length=456, verbose_name='评论', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadTag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('read_tag', models.CharField(max_length=12, verbose_name='文章标签')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
                'db_table': 'read_tag',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(verbose_name='所属文章', to='yuedu.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='read_tag_info',
            field=models.ManyToManyField(to='yuedu.ReadTag', verbose_name='文章的标签'),
        ),
    ]
