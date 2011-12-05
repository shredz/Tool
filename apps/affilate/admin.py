from apps.affilate.models import Affilate
from django.contrib import admin
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
from django import template
from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
import settings

from django.http import HttpResponseRedirect
from django.contrib import messages


# Imaginary function to handle an uploaded file.

      
class AffilateAdmin(admin.ModelAdmin):
    list_display = ('program','affilate_name')
    #search_fields = ['title']
    #list_filter = ['category']
    #change_list_template = 'spiffs/admin/deallist.html'
admin.site.register(Affilate, AffilateAdmin )