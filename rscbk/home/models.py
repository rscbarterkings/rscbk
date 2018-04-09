# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Brand(models.Model):
    DEFAULT_PK=1
    brand_name = models.CharField(max_length=15, help_text='brand name')

    def __str__(self):
        return '{0}'.format(self.brand_name)


# Create your models here.
