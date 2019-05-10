# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('detail', tinymce.models.HTMLField(verbose_name='文章', blank=True)),
                ('title', models.CharField(verbose_name='文章标题', max_length=10)),
                ('readcount', models.IntegerField(verbose_name='阅读量', default=0)),
                ('comment', models.CharField(verbose_name='评论', max_length=256, blank=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='ReadType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('type', models.CharField(verbose_name='文章类型', max_length=10)),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
                'db_table': 'read_type',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='read_type',
            field=models.ForeignKey(verbose_name='文章分类', to='yuedu.ReadType'),
        ),
    ]
