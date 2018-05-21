# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Brand,UserFullProfile,Feedback


@admin.register(UserFullProfile)
class UserFullProfileAdmin(admin.ModelAdmin):
    list_display = ['mobile','user']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display =['customer_name', 'comment']
