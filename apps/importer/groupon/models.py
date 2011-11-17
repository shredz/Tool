from django.db import models
import datetime
from decimal import *

class Gp_Location(models.Model):
    latitude = models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    longitude = models.DecimalField(max_length=10,decimal_places=4,max_digits=10)
    location_name = models.CharField(max_length=30)
    timezone = models.CharField(max_length=30)
    location_id = models.CharField(max_length=30)
    def __unicode__(self):
        return self.location_name
class Gp_Country(models.Model):
    title             = models.CharField(max_length=20)
    ph_code            = models.IntegerField(max_length=5)
    continent        = models.CharField(max_length=15)
    #flag            = models.FileField(blank=True)
    location        = models.ForeignKey(Gp_Location,null=True)

    def __unicode__(self):
        return self.title

class Gp_Merchant(models.Model):
    merchant_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    websiteUrl = models.URLField()
    
    def __unicode__(self):
        return self.name

class Gp_Address(models.Model):
    zipcode = models.CharField(max_length=7)
    street_line_1 = models.CharField(max_length=30)
    street_line_2 = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    country    = models.ForeignKey(Gp_Country, null=True)
    phonenumber    = models.CharField(max_length=50)
    location = models.ForeignKey(Gp_Location, null=True)
    def __unicode__(self):
        return self.city

class Gp_Deal(models.Model):
	deal_id = models.CharField(max_length=30)
	title = models.CharField(max_length=200)
	status = models.CharField(max_length=30)
	description = models.TextField()
	location = models.ForeignKey(Gp_Location, null=True)
	deal_open   = models.DateTimeField(db_index=True)
	deal_close  = models.DateTimeField(db_index=True)
	total_sold  = models.IntegerField()
	currency = models.CharField(max_length=30)
	is_free     = models.BooleanField(default=False)    
	is_featured = models.BooleanField(default=False, db_index=True)
	highlights  = models.TextField(null=True)
	purchase_url = models.URLField(verify_exists=False, unique=True)
	reward_points  = models.IntegerField(default=0)
	pitchhtml = models.TextField(null=True)
	image_urls= models.URLField()
	tags= models.CharField(max_length=200)
	merchant= models.ForeignKey(Gp_Merchant, null=True)
	address = models.ForeignKey(Gp_Address,null=True)

	@staticmethod
	def front_page(page,layout):
		now = datetime.datetime.now()
		layout = str(layout)
		
		if layout == "1":
			total = 4
			names = ["deal1","deal2","deal3","deal4"]	
		
		elif layout == "2":
			total = 8
			names = ["deal1","deal2","deal3","deal7","deal8", "deal4","deal6","deal5"]
			
		elif layout == "3":
			total = 8
			names = ["deal1","deal2","deal3","deal4","deal5","deal6","deal7","deal8"]
		
		deals = Gp_Deal.objects.filter(deal_open__lte=now, deal_close__gte = now).extra(order_by=['deal_open'])[(page-1)*total:(page*total)]
			
		ds = {}
		count = 0
		
		
		#deals = Deal.assign_left(deals)
		
		for deal in deals:
			deal.option = deal.options.all()[0]
			discount = ((deal.option.value - deal.option.price) / deal.option.value) * Decimal(100.00)
			discount = float(discount)
			deal.discount = discount - discount % 0.01 
			
			ds[names[count]] = deal
			count = count + 1
		
		return (ds,names)
		
	def __unicode__(self):
		return self.title
        
class Gp_Deal_Options(models.Model):
    option_id = models.IntegerField() 
    title = models.CharField(max_length = 200)
    buy_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateTimeField()
    deal = models.ForeignKey(Gp_Deal,related_name="options")
    def __unicode__(self):
        return self.title
