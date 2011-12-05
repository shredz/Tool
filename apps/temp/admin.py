from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import admin
from apps.temp.models import Temp
from apps.core.models import SpiffObject,SpiffTicket
from django import forms
from apps.spiffs.models import Deal
from django import template
from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
import settings
import csv
from django.http import HttpResponseRedirect
from django.utils.safestring import *



def importfile(request, *callback_args, **callback_kwargs) :
	
	from django.db import connection, transaction
        cursor = connection.cursor()
	#cursor.execute("UPDATE core_spiffobject SET description = 'anuj.'","id =366")
        #arr = cursor.fetchone()

	#filenameval =''
	#cursor=connection.cursor()
	intidval2 = 0
	inc       = 0
	#intidval2 = int(intidval2)
	#cursor.execute("UPDATE core_spiffobject SET description =  %s WHERE id = %s", ['Enjoy a fiery Mexican feast with $10 worth of menu items at Jalpa Mexican Restaurant for just $4 at 60% off.', '366'])
        #SpiffObject.objects.filter(id=366).update(description='Enjoy a fiery Mexican feast with $10 worth of menu items at Jalpa Mexican Restaurant for just $4 at 60% off.')
	#return render_to_response('temp/admin/importfile.html', {'run_list': tempres,'run_list2': 'fff'})
	latest_poll_list = Temp.objects.all()
     	#t = loader.get_template('temp/admin/importfile.html')
     	for file in latest_poll_list:
    		filenameval = file.filename
    	response1 = HttpResponse(mimetype='text/csv')
	file=open(str(filenameval))	
	testReader = csv.reader(file ,delimiter='~', quotechar='|')
	for filetext in testReader:
    		#for filetext2 in filetext:
		if inc >0:
			filedatatitle = filetext[0].lstrip('","')
			filedatadescription = filetext[1].lstrip('",')
			filedatadescription = filedatadescription.lstrip('","')
			filedatacat         = filetext[2].lstrip('","')
			filedataapprove     = filetext[3].lstrip('","')
			priceval            = filetext[5].lstrip('","')
			intidval            = filetext[6].lstrip('","')
			if intidval.isdigit():
			       intidval2 = int(intidval)
		
		
               # return intidval
		#Temp.objects.raw("UPDATE `core_spiffobject` SET `description` = 'Enjoy a fiery Mexican feast with $10 worth of menu items at Jalpa Mexican Restaurant for just $4 at 60% off.' WHERE `id` =366;")
			SpiffObject.objects.filter(id = intidval2).update(description=filedatadescription,title=filedatatitle)
			Deal.objects.filter(id = intidval2).update(price=priceval)
		inc +=1
        #return render_to_response('temp/admin/importfile.html', {'run_list': filetext[1]})
	return HttpResponseRedirect("/admin/spiffs/deal/")

	        
   		
class TempAdmin(admin.ModelAdmin):
    
    change_form_template = 'temp/admin/edit.html'
    
    def get_osm_info(self):
        # ...
        pass

    def change_view(self, request, object_id, extra_context=None):
        value = "dfd";
        my_context = {
            'osm_data': self.get_osm_info(),
            'ddd': '',
        }
        return super(TempAdmin, self).change_view(request, object_id,
            extra_context=my_context)
            
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
            
admin.site.register(Temp, TempAdmin)        