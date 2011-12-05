from django.db import models
from django.contrib import admin

import settings

class Country(models.Model):
	country_name =  models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.country_name

#admin.site.register(Point)

class State(models.Model):
	state_name    = models.CharField(max_length=100)
	country_id    = models.ForeignKey('Country')
	
        
	def __unicode__(self):
		return self.state_name
	
#admin.site.register(Rule)
	
class City(models.Model):
	city_name 	        = models.CharField(max_length=100)
	state_id		= models.ForeignKey('State')
        
	
	def __unicode__(self):
		return self.city_name
            
            
class Address_deal_map(models.Model):
	address 	= models.CharField(max_length=500)
	city_id		= models.ForeignKey('City')
        deal_id		= models.ForeignKey('core.SpiffObject')
        country_id      = models.ForeignKey('Country')
        longitude       = models.DecimalField(max_digits=6, decimal_places=5)
        latitude        = models.DecimalField(max_digits=6, decimal_places=5)
        
	
	def __coerce__(self):
		return self.deal_id

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Address_deal_map)

