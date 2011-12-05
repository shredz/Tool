from django.db import connection
from apps.core.models import Category
from apps.core.models import SpiffObject
from django.contrib.admin.sites import AdminSite
from apps.spiffs.models import Deal
from django.contrib import admin
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
from django import template
from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
import settings
import csv
from django.http import HttpResponseRedirect
from django.contrib import messages


# Imaginary function to handle an uploaded file.



def export(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'
	
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description','Category', 'Approved', 'Advertiser Name','Price', 'id'])
    
    deal_list = Deal.objects.all()
    thumbnail_list = []
    for file in deal_list:
    	title = file.title +"~"
    	description = file.description+"~"
    	approved = str(file.approved) +"~"
    	category = str(file.category) +"~"
    	advertiser_name = file.advertiser_name+"~"
	price = str(file.price)+"~"
        id = file.id
        writer.writerow([title.encode('utf8'),description.encode('utf8'), category, approved,advertiser_name,price,id ])
    return response
    
def importfiletemp(request):
	    file=open("/var/django/spiffcity_dev/resources/static/media/uploads/export.csv")
	
	    testReader=csv.reader(file,delimiter=',', quotechar='|')
	    for row in testReader:
	      return render_to_response('spiffs/admin/importfile.html', {'run_list': testReader,'run_list2': 'fff'})
	      
def importfile(request):
	   		file=open("/var/django/spiffcity_dev/resources/static/media/uploads/export.csv")
	   		testReader=csv.reader(file,delimiter=',', quotechar='|')
	   		return render_to_response('spiffs/admin/importfile.html', {'run_list': testReader,'run_list2': 'fff'})

def assigncat(request):
    p = request.POST['catdd'].split('=')
    #r = request.POST.get('_selected_action')
    dealsid = request.POST.getlist('_selected_action')
    listval = []
   
    #value = r.split('_selected_action')_selected_action
    #r = ', '.join([p for p in request.POST['_selected_action']])
    
    cat_id = p[1]
    #SpiffObject.objects.filter(id='366').update(category=cat_id)
    for id in dealsid:
	idval = id
	SpiffObject.objects.filter(id=idval).update(category=cat_id)
    test2 = request.path
    
    #request.flash['notice'] = 'Category is assign'
    #messages.success(request, 'Category assign succesfully.')
    #return render_to_response('admin/test.html',{'p':test2})
    return HttpResponseRedirect("/admin/spiffs/deal/")

   
class DealAdmin(admin.ModelAdmin):
    change_list_template = 'spiffs/admin/deallist.html'
    def changelist_view(self, request, extra_context=None):
        para_list = Category.objects.values('parent','title','id').filter(parent=1).distinct('parent')
        my_context = { 'para_list': para_list,
                      }
        return super(DealAdmin, self).changelist_view(request, extra_context=my_context)
    
    list_display = ('title','advertiser_name','categories','price','address','discount','approved','date')
    search_fields = ['title']
    list_filter = ['category']
    list_per_page = 20
    
    
    
        
admin.site.register(Deal,DealAdmin)


