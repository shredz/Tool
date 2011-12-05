from django.db import models
from django.contrib import admin
from django import forms

import settings

class Point(models.Model):
	point_percentage		=  models.DecimalField(max_digits=5, decimal_places=2)
	
	def __unicode__(self):
		return "%d" % self.point_percentage

#admin.site.register(Point)

class Rule(models.Model):
	point_percentage 		    = models.ForeignKey('Point')
	commission_percentage_range_from    = models.IntegerField()
	commission_percentage_range_to      = models.IntegerField()
        
	def __unicode__(self):
		#return self.commission_percentage_range_from
	        return "%d" % self.commission_percentage_range_from
	
#admin.site.register(Rule)

class PointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PointForm, self).__init__(*args, **kwargs)
        self.fields['point_percentage'].label = 'What song are you going to sing?'

    class Meta:
        model = Point


	
#class Userpointdetail(models.Model):
#	deal 	        = models.ForeignKey('spiffs.Deal')
#	user		= models.ForeignKey('members.User')
#        point		= models.DecimalField(max_digits=5, decimal_places=2)
	
#	def __unicode__(self):
#		return self.deal

#admin.site.register(Userpointdetail)

