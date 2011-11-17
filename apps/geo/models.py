from django.db import models
from django.contrib import admin

import settings

class Country(models.Model):
	title 			= models.CharField(max_length=20)
	ph_code			= models.IntegerField(max_length=5)
	continent		= models.CharField(max_length=15,choices=settings.ENUMS['CONTINENTS'])
	flag			= models.FileField(upload_to=settings.FLAGPATH,blank=True)
	location		= models.ForeignKey('geo.Location',null=True)
	
	@staticmethod
	def list_for_dropdown():
		ls = []
		for c in Country.objects.all():
			ls.append((c.id,c.title))
			
		return ls
	
	def __unicode__(self):
		return self.title




class Address(models.Model):
	zipcode 		= models.CharField(max_length=7)
	street_line_1	= models.CharField(max_length=30)
	street_line_2	= models.CharField(max_length=30)
	city			= models.CharField(max_length=25)
	state			= models.CharField(max_length=20)
	country			= models.ForeignKey('geo.Country')
	phonenumebr 	= models.ForeignKey('core.PhoneNumber')
	location 		= models.ForeignKey('geo.Location')
	
class Location(models.Model):
	latitude 		= models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
	longitude		= models.DecimalField(max_length=10,decimal_places=4,max_digits=10)

try:
	admin.site.register(Country)
	admin.site.register(Location)
except:
	pass
