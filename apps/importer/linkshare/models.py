from django.db import models

from apps.spiffs.models import Deal

class LDealManager(models.Manager):
	def list_page (self, page , total):
		return LDeal.objects.filter(approved=True).extra(order_by=['id'])[(page-1)*total:(page*total)]


class LDeal(Deal):
	description_short		=	models.CharField(max_length=255)
	deal_open 				= 	models.DateTimeField()

	objects					=  LDealManager()
	"""
    sku  :  2014
	category  :  {u'primary': u' Los Angeles - South Bay ', u'secondary': u'  Health & Fitness '}
	merchantname  :  YourBestDeals.com
	linkid  :  2014
	createdon  :  2011-08-20/14:45:15
	mid  :  36553
	productname  :   Dr. David Beber - Torrance 
	imageurl  :  http://www.yourbestdeals.com/images/1cea0324-af6c-4655-a6a9-90e92dc03b69.jpg
	currency  :  USD
	linkurl  :  http://click.linksynergy.com/fs-bin/click?id=lmLSmH4npyk&offerid=214427.2014&type=15&subid=0
	price  :  1092
	description  :  {u'short': u'You Have Never Seen A Great Dental Deal Like This Before!  Full Mouth X-Rays, Exam, Cleaning, In Office Whitening Treatment, AND a Smile Enhancment Take Home Kit!  For Only $149.00!', u'long': u"By appointment only with coupon code ready.  No cash value or cash back.  Can't be combined with any other offers.  Expires one year from date of purchase.  Rescheduling, no show, or cancellation will forfeit your coupon."}
	"""
    
	def __unicode__(self):
		return self.title
