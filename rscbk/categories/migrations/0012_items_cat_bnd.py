# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_categorybrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='cat_bnd',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.CategoryBrand'),
        ),
    ]