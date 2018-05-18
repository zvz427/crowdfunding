# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-18 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20180515_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='TageOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tage_type', models.CharField(default='手机', max_length=10, verbose_name='项目一级标签')),
            ],
            options={
                'verbose_name_plural': '项目一级标签属性',
                'verbose_name': '项目一级标签属性',
            },
        ),
        migrations.CreateModel(
            name='TageTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tage_type', models.CharField(default='贴膜', max_length=10, verbose_name='项目二级标签')),
            ],
            options={
                'verbose_name_plural': '项目二级标签属性',
                'verbose_name': '项目二级标签属性',
            },
        ),
        migrations.RemoveField(
            model_name='tage',
            name='project',
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='active_status',
            field=models.CharField(choices=[('0', '即将开始'), ('1', '众筹中'), ('2', '众筹成功')], default='0', max_length=10, verbose_name='项目众筹状态'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='check_status',
            field=models.CharField(choices=[('0', '审核中'), ('1', '审核通过'), ('2', '审核未通过')], default='0', max_length=10, verbose_name='项目审核状态'),
        ),
        migrations.DeleteModel(
            name='Tage',
        ),
        migrations.AddField(
            model_name='tagetwo',
            name='project',
            field=models.ManyToManyField(default=1, to='project.ProjectInfo', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='tagetwo',
            name='tage_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.TageOne', verbose_name='父级标签'),
        ),
        migrations.AddField(
            model_name='tageone',
            name='project',
            field=models.ManyToManyField(default=1, to='project.ProjectInfo', verbose_name='项目'),
        ),
    ]
