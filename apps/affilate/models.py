from django.db import models
from django.contrib import admin

import settings

class Affilate(models.Model):
	program		=  models.CharField(max_length=150)
	affilate_name   = models.CharField(max_length=150)
	def __unicode__(self):
	    return self.program