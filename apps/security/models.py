from django.db import models	
from django.contrib import admin

class AllowedHosts (models.Model):
	ip 		= models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.ip


try:
	admin.site.register(AllowedHosts)
except:
	pass	
