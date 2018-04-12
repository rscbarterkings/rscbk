# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_items_bnd'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_brand_name', models.CharField(help_text='brand name', max_length=15)),
            ],
        ),
    ]