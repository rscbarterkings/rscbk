# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_items_itemuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_status',
            field=models.CharField(choices=[('A', 'Available'), ('S', 'Sold out')], default='A', help_text='Current Item Status', max_length=3),
        ),
    ]
