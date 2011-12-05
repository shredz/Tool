from apps.core.models import Category
from apps.core.models import SpiffObject
from apps.point.models import Point, Rule
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

      
class PointAdmin(admin.ModelAdmin):
    
    list_display = ['point_percentage']
admin.site.register(Point,PointAdmin)

class RuleAdmin(admin.ModelAdmin):
    change_form_template = 'point/admin/change_edit.html'
    list_display = ('point_percentage','commission_percentage_range_from','commission_percentage_range_to')
    
admin.site.register(Rule,RuleAdmin)


#class UserpointdetailAdmin(admin.ModelAdmin):
    
 #   list_display = ['point']
    
#admin.site.register(Userpointdetail,UserpointdetailAdmin)
