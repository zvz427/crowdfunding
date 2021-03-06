# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-11 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180511_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercertify',
            name='id_card',
            field=models.CharField(default=0, max_length=18, verbose_name='用户身份证号'),
        ),
        migrations.AlterField(
            model_name='usercertify',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='usercertify',
            name='realname',
            field=models.CharField(default='', max_length=50, verbose_name='用户真实姓名'),
        ),
        migrations.AlterField(
            model_name='usercertify',
            name='realname_certify',
            field=models.CharField(choices=[('0', '未实名认证'), ('1', '已实名认证')], default='0', max_length=10, verbose_name='用户实名认证'),
        ),
        migrations.AlterField(
            model_name='usercertify',
            name='usercertify_type',
            field=models.CharField(choices=[('GovernmentAndNoprofitOrganizations', '政府及非营利组织'), ('PersonalManagement', '个人经营'), ('IndividualIndustryAndCommerce', '个体工商户'), ('BusinessCompany', '商业公司')], max_length=100, verbose_name='实名认证账户类型'),
        ),
    ]
