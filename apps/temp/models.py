from django.db import models
from django.contrib import admin
from django.db.models import Q
import settings
from apps.members.models import UserPoint
import datetime


class Temp(models.Model):
	filename  = models.FileField(upload_to="/var/django/spiffcity_dev/resources/static/media/uploads")
	def force_unicode(self):
		return self.filename 