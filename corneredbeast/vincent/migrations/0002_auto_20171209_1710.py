# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-09 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vincent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weidongurls',
            name='create_user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='weidongurls',
            name='business',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='weidongurls',
            name='category',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='weidongurls',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weidongurls',
            name='flag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='belongtourl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vincent.weidongurls'),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='environment',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='flag',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='nickname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='password',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='phone',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='portrait',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='weidongusers',
            name='username',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]