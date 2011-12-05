from apps.core.models import Category
from django.contrib import admin
from django import forms
import settings
import os
from django.utils.html import escape


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','maincategory','thumbnail','thumbnail2')
    #list_display = ['title']
    search_fields = ['title']
    change_list_template = 'core/admin/list.html'
    #result_list_template = 'core/admin/change_list_new_results.html'
    
admin.site.register(Category, CategoryAdmin)

