# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='[NO NAME]', max_length=255)),
                ('titlethumb', models.CharField(default='', max_length=2000)),
                ('titlecard', models.CharField(default='', max_length=2000)),
                ('logopath', models.CharField(default='', max_length=255)),
                ('explainpath', models.CharField(default='', max_length=255)),
                ('explainpath2', models.CharField(default='', max_length=255)),
                ('tspath', models.CharField(default='', max_length=255)),
                ('templatepath', models.CharField(default='', max_length=255)),
                ('participation', models.CharField(default='', max_length=20)),
                ('coupon', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('longname', models.CharField(default='', max_length=500)),
                ('url', models.CharField(default='', max_length=500)),
                ('imgpath', models.CharField(default='', max_length=255)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ManyToManyField(to='story.Provider'),
        ),
    ]
