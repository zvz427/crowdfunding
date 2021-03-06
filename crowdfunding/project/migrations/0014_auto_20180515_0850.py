# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-15 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20180514_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='check_status',
            field=models.CharField(choices=[('0', '审核中'), ('2', '审核未通过'), ('1', '审核通过')], default='0', max_length=10, verbose_name='项目审核状态'),
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='is_del',
            field=models.BooleanField(default=True, verbose_name='标记删除'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='active_status',
            field=models.CharField(choices=[('0', '即将开始'), ('2', '众筹成功'), ('1', '众筹中')], default='0', max_length=10, verbose_name='项目众筹状态'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='category',
            field=models.CharField(choices=[('public_welfare', '公益'), ('technology', '科技'), ('agriculture', '农业'), ('culture', '文化'), ('design', '设计')], default='technology', max_length=20, verbose_name='项目分类'),
        ),
    ]
