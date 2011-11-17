from django.db import models
from django.contrib import admin
from django.db.models import Q

import settings
from apps.core.models import SpiffObject,SpiffTicket
from apps.members.models import UserPoint

import datetime

class DealManager(models.Manager):
	
	def list_page (self, page , total):
		return self.get_query_set().filter(approved=True).extra(order_by=['id'])[(page-1)*total:(page*total)]

	def list_new  (self, page, total):
		return self.get_query_set().filter(approved=False).extra(order_by=['id'])[(page-1)*total:(page*total)]
		
		
#---------------------------------------------------------

class UserDeal(models.Model):
	user				= models.ForeignKey('members.User')
	deal				= models.ForeignKey('spiffs.Deal')
	added				= models.DateTimeField(auto_now_add=True)

#---------------------------------------------------------

class DealVisit(models.Model):
	user				= models.CharField(max_length=10)
	deal				= models.ForeignKey('spiffs.Deal')
	visited				= models.DateTimeField(auto_now_add=True)
	reported			= models.DateTimeField(auto_now_add=True)
	status				= models.CharField(max_length=10, choices=settings.ENUMS["VISIT_STATES"], default="VISITED")

#---------------------------------------------------------

class Deal(SpiffObject):
	sku 				= models.CharField(max_length=50)
	deal_id 			= models.CharField(max_length=30)
	advertiser_name 	= models.CharField(max_length=200)
	price 				= models.DecimalField(max_digits=10, decimal_places=2)
	currency 			= models.CharField(max_length=30)
	mid					= models.CharField(max_length=50)
	
	objects				= DealManager()
	
	def __unicode__(self):
		return self.title
		
	def shared (self, user):
		at = ActivityType.objects.get(title="SHARED_DEAL")
		sa = ShareActivity(user=user,activity_type=at,deal=self,points=2,network="facebook")
		sa.save()
		user.award_points(sa)
		
		
	
	def buy (self,user):
		ud = UserDeal(user=user, deal=self)
		ud.save()
		at = ActivityType.objects.get(title="BOUGHT_DEAL")
		sa = SpiffActivity(user=user,activity_type=at,userdeal=ud,points=deal.points)
		sa.save()
		user.award_points(sa)
		
		
	def is_valid(self):
		now = datetime.datetime.now()
		return now >= self.deal_open and now <= self.deal_close
	
	@staticmethod
	def assign_left(deals):
		now = datetime.datetime.now()
		
		ls = []
		
		for deal in deals:
			td = deal.expiration_date - now
			left = {}
			left["days"] = td.days
			left["hours"] = td.seconds / 3600
			left["mins"] = (td.seconds % 3600) / 60
			
			deal.left = left
			
			ls.append(deal)
		
		return ls
	
	@staticmethod
	def search(keyword):
		deals = Deal.objects.filter(Q(title__contains=keyword)| Q(description__contains=keyword))
		return Deal.assign_left(deals)
	
	
	
	

admin.site.register(Deal)		

class Coupon(SpiffTicket):
	deal			= models.ForeignKey(Deal, related_name='coupons')
	title			= models.CharField(max_length=255)
	
	def is_expired(self):
		return datetime.date.today() > self.expiration_date
		

class ActivityType(models.Model):
	title 			= models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title

admin.site.register(ActivityType)


class RewardType(models.Model):
	title 			= models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title
	
class Reward(models.Model):
	reward_type		= models.ForeignKey(RewardType)
	activity		= models.ForeignKey('spiffs.Activity')
	


class Activity(models.Model):
	activity_type	= models.ForeignKey(ActivityType)
	user			= models.ForeignKey('members.User')
	added			= models.DateTimeField(auto_now_add=True)
		
	@staticmethod
	def get_delta_range(var,val):
		if var == "days":
			f = datetime.timedelta(days=val-1)
			t = datetime.timedelta(days=val)
		elif var == "months":
			f = datetime.timedelta(months=val-1)
			t = datetime.timedelta(months=val)
		
		return (f,t)
	
	def child(self):
		try:
			return ShareActivity.objects.get(id=self.id)
		except:
			try:
				return SpiffActivity.objects.get(id=self.id)
			except:
				return self
	
	@staticmethod
	def recent (user,limit):
		userpoints = UserPoint.objects.filter(user=user)[:5]
		ls = []
		for up in userpoints:
			up.activity = up.activity.child()
			ls.append(up)
		return ls
		
		"""
		activities =  Activity.objects.filter(user=user).extra(order_by=['-added'])[:5]
		ls = []
		for activity in activities:
			activity = activity.child()
			up = activity.userpoints.all()[0]
			up.activity = activity
			ls.append(up)
		return ls		
		"""
		
	@staticmethod
	def chart(user,limit,sortby="days"):
		ls = {}
		now = datetime.datetime.now()
		for i in range(limit):
			time_range = Activity.get_delta_range(sortby,i)
			ls[now-time_range[0]]=Activity.objects.filter(user=user,added__gt=now-time_range[0],added__lte=now-time_range[1]).count()
		
		return ls

class ShareActivity(Activity):
	deal			= models.ForeignKey(Deal)
	network			= models.CharField(max_length=20)

class SpiffActivity(Activity):
	userdeal		= models.ForeignKey(UserDeal)
	points			= models.DecimalField(max_digits=5, decimal_places=2)
	points_status	= models.CharField(max_length=15, choices=settings.ENUMS["POINT_STATUS"], default="PENDING")

