# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='category_one',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='food_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='r_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='yelp_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age_range',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='education',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hometown',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='num_friends',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='religion',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='term',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
