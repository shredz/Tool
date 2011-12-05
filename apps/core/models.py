from django.db import models
from django.contrib import admin
#from PIL import Image as PImage
import os
import settings

#**************************************#
#	managers

class CategoryManager(models.Manager):

	def get_categories(self, number):
		return super(CategoryManager, self).get_query_set().filter(parent=number)

	def get_descendants(self, parent_id):
		ls ={}
		descs = self.get_categories(parent_id)
		
		for node in descs:
		    if node.id !=1:    
		        ls[node] = self.get_descendants(node.id)
		
		return ls

	def get_category_items(self, list):
		items = set()
		for key,val in list.items():
			items.update(Cat_Items.objects.filter(category_id = key.id))
			if val:
				items.update(self.get_category_items(val))
		return items
		
#**************************************#


class DisplayObject(models.Model):
	title		= models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	display		= models.FileField(upload_to=settings.MEDIA_UPLOAD_PATH)
	root		= models.ForeignKey('members.User',related_name='owned_displayobjects')
	admins		= models.ManyToManyField('members.User',related_name='administrated_displayobjects')

class PhoneNumber(models.Model):
	countrycode = models.IntegerField(max_length=5)
	carriercode = models.IntegerField(max_length=5)
	number 		= models.IntegerField(max_length=9)

class Verification(models.Model):
	purpose		= models.CharField(max_length=1, null=True, choices=settings.ENUMS["VERIFICATION_PURPOSE"])
	code 		= models.CharField(max_length=12)
	verified	= models.BooleanField(default=False)
	verified_on = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
	title 		= models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	parent		= models.ForeignKey('self')
	image1		= models.FileField(upload_to=settings.CAT_IMAGE_PATH,blank=True)
	image2		= models.FileField(upload_to=settings.CAT_IMAGE_PATH,blank=True)
	objects		= CategoryManager()
		
	#def admin_src(self):
	#image_src = "<img id='firstid' width='52' height='22' src='http://cdndev.spiffcity.com/media/%s'> "% self.src
	#	return image_src;
	#	src.allow_tags=True
		
	def thumbnail(self):
		#return '<img border="0" alt="" src="http://cdndev.spiffcity.com/media/%s" height="40" />' % ((self.image1))
		return "<img border='0' alt='' src='http://cdndev.spiffcity.com/media/%s' height='40' />" % ((self.image1))
		#return valu.encode('utf-8')
		thumbnail.allow_tags = True
	def thumbnail2(self):
		#return '<img border="0" alt="" src="http://cdndev.spiffcity.com/media/%s" height="40" />' % ((self.image1))
		return "<img border='0' alt='' src='http://cdndev.spiffcity.com/media/%s' height='40' />" % ((self.image2))
		#return valu.encode('utf-8')
		thumbnail2.allow_tags = True
	def maincategory(self):
		#return '<img border="0" alt="" src="http://cdndev.spiffcity.com/media/%s" height="40" />' % ((self.image1))
		return self.parent
		#return valu.encode('utf-8')
		maincategory.allow_tags = True
	
	def __unicode__ (self):
		return self.title
		


#admin.site.register(Category)


class SpiffObject(models.Model):
	title		= models.CharField(max_length=100)
	description = models.TextField()
	category	= models.ForeignKey(Category)
	image_url	= models.URLField(verify_exists=False)
	purchase_url= models.URLField(verify_exists=False)
	approved	= models.BooleanField(default=False)
	is_free 	= models.BooleanField(default=False)	
	is_featured = models.BooleanField(default=False)

	#class Meta:
	#	abstract = True
		
	def __unicode__(self):
		return self.title

class SpiffTicket(models.Model):
	spiffobject 	= models.ForeignKey(SpiffObject)
	created 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True, auto_now_add=True)
	expiration_date	= models.DateField()
	
	user			= models.ForeignKey('members.User')
	
	price_amount	= models.DecimalField(max_digits=6, decimal_places=2)
	price_currency	= models.CharField(max_length=3, default='USD')
	
	value_amount	= models.DecimalField(max_digits=6, decimal_places=2)
	value_currency	= models.CharField(max_length=3, default='USD')
	
	purchase_min	= models.IntegerField(default=1)
	purchase_limit	= models.IntegerField(default=0)
	
	total_available	= models.IntegerField(default=-1) # Reserved for later implementation, limited availability
	total_sold		= models.IntegerField(default=0)
	purchase_url	= models.URLField(verify_exists=False) # Don't verify, assume valid
	full_details	= models.TextField()
	reward_points	= models.IntegerField(default=0)
	

#admin.site.register(Category)