from django.db import models

from apps.spiffs.models import Deal, DealVisit
from libs.utils import ValueManager

import settings, time

class Report (models.Model):
	
	created 				= models.DateTimeField(auto_now_add=True)
	updated 				= models.DateTimeField(auto_now=True, auto_now_add=True)
	locked					= models.DateTimeField()
	posted					= models.DateTimeField()
	eventoccured			= models.DateTimeField()
		
	deal					= models.ForeignKey(Deal, related_name="reports")
	sid						= models.CharField(max_length=25)
	visit					= models.ForeignKey(DealVisit)
	
	original				= models.BooleanField(default=True)	
	original_action_id		= models.CharField(max_length=10)
	transaction_id			= models.CharField(max_length=10)
	order_id				= models.CharField(max_length=25)
	
	action_type				= models.CharField(max_length=15)	
	action_status			= models.CharField(max_length=15)	
	
	
	country					= models.CharField(max_length=20)	
	website_id				= models.CharField(max_length=10)
	
	sale_amount				= models.DecimalField(max_digits=10, decimal_places=4)
	commission_amount		= models.DecimalField(max_digits=10, decimal_places=4)
	
	
	
	@staticmethod
	def create_from_dic (report):
		try:
			dv = DealVisit.objects.get(id = report["sId"])
			spiffobject		= dv.deal
			
		except DealVisit.DoesNotExist, dne:
			print "DealVisit with id %s does not exist" % (report["sId"])
			return None	

		try:
			print "seacrhing report = ",report["sId"]
			return Report.objects.get(sid = report["sId"])
		except Report.DoesNotExist, dne:
			print "Report with %s does not exist so, will create one " % (report["sId"])
			
			f1 = "%Y-%m-%dT%H:%M:%S"
			f2 = "%Y-%m-%d %H:%M"
			
			rep = Report(
				locked 			= ValueManager.format_date(report["lockingDate"],f1,f2,"-"),
				posted 			= ValueManager.format_date(report["postingDate"],f1,f2,"-"),
				eventoccured 	= ValueManager.format_date(report["eventDate"],  f1,f2,"-"),	
				
				deal			= spiffobject,
				visit			= dv,
				sid				= report["sId"],
				
				original		= report["original"],
				original_action_id	=report["originalActionId"],
				transaction_id	= report["transactionId"],
				order_id		= report["orderId"],
				action_type 	= report["actionType"],
				action_status	= report["actionStatus"],
				country			= report["country"],
				website_id		= report["websiteId"],
				sale_amount		= report["saleAmount"],
				commission_amount=report["commissionAmount"],
			)
		
			rep.save()
			return rep
