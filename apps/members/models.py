#django
from django.db import models
from django.contrib.auth.models import User,UserManager, get_hexdigest
from django.contrib import admin
from django.core.mail import send_mail

#project
import settings

#models
from apps.core.models import *


class ConfigType(models.Model):
	title				= models.CharField(max_length=20)
	description			= models.CharField(max_length=50)
	default				= models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.title


class Config(models.Model):
	user				= models.ForeignKey('members.User')
	configtype			= models.ForeignKey('members.ConfigType')
	value				= models.CharField(max_length=100,blank=True) 
	

class Referral(models.Model):
	reffered_by			= models.ForeignKey('members.User',related_name='reffered_to')
	reffered_to			= models.ForeignKey('members.User',related_name='reffered_by')
	
		
	created				= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True,auto_now_add=True)	
	
	def __unicode__(self):
		return self.reffered_by.username+" => "+self.reffered_to.username
	
class UserPoint(models.Model):
	user 				= models.ForeignKey('members.User')
	activity			= models.ForeignKey('spiffs.Activity',related_name="userpoints")
	points				= models.DecimalField(max_digits=5, decimal_places=2)
	
	#created				= models.DateTimeField(auto_now_add=True)
	#updated				= models.DateTimeField(auto_now=True,auto_now_add=True)
	
class User (User):
	gender 				= models.CharField(max_length=1, null=True, choices=settings.ENUMS["GENDER"])
	dob 				= models.DateField()

	points				= models.DecimalField(max_digits=10, decimal_places=2)
	
	verification		= models.ForeignKey('core.Verification')
	address 			= models.ForeignKey('geo.Address')
	
	friends				= models.ManyToManyField('self')
	
	"""
	def points(self, LIMIT=-1):
		points = UserPoint.objects.raw("SELECT * FROM members_userpoint AS p , spiffs_activity AS a WHERE p.activity_id = a.id AND a.user_id = %d" %(self.id))[:LIMIT]
		return points
	"""
	
	def send_verification_mail(self):
		link = 'http://dev.spiffcity.com/members/v/'+str(self.verification.code)+"/"
		send_mail('Spiffcity Verification Link', link , 'webmaster@spiffcity.com',
    [self.email], fail_silently=True)
	
	def get_refferer(self,degree=1):
		reffered_to = self
		for i in range(degree):
			try:
				reffered_to = Referral.objects.get(reffered_to=reffered_to).reffered_by
			except Referral.DoesNotExist:
				return None
		return reffered_to
	
	def award_points (self,spiff_activity,degree=0):
		if degree < 1:
			degree = settings.POINTS_SYS['MAX_DEGREE']
			
		up = UserPoint(user=self,activity=spiff_activity,points=spiff_activity.points)
		up.save()
		
		for i in range(degree):
			j = i+1
			ref = self.get_refferer(j)
			if ref is not None:
				up = UserPoint(user=ref,activity=spiff_activity,points=spiff_activity.points/(j+1))
				up.save()
			
	
	def get_all_config(self):
		config = {}
		for ctype in ConfigType.objects.all():
			try:
				c = Config.objects.get(user=self,configtype=ctype)
			except:
				c = Config(user=self,configtype=ctype,value=ctype.default)
				c.save()
			config[c.configtype.title] = c
		return config
	
	def get_config(self,ctype):
		ctype = ConfigType.objects.get(title=ctype)
		try:
			c = Config.objects.get(user=self,configtype=ctype)
		except:
			c = Config(user=self,configtype=ctype,value=ctype.default)
			c.save()
		return c
	
	def set_config(self,ctype,value):
		ctype = ConfigType.objects.get(title=ctype)
		try:
			c = Config.objects.get(user=self,configtype=ctype)
		except:
			c = Config(user=self,configtype=ctype)
			c.save()
		c.value=value
	

	@staticmethod
	def instance (user):
		return User.objects.get(id=user.id)
	
	@staticmethod
	def instance_from_id (userid):
		return User.objects.get(id=userid)
	
	@staticmethod
	def encode_pass(raw):
		import random
		algo = 'sha1'
		salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
		hsh = get_hexdigest(algo, salt, raw)
		password = algo+'$'+salt+'$'+hsh
		return password
	
	@staticmethod
	def create_verification (vtype,verified=False):
		v = Verification (
			purpose		= vtype,
			code		= UserManager().make_random_password(12),
			verified 	= verified,
		)
		v.save()
		return v
		


class Prospect(models.Model):
	email				= models.EmailField(max_length=75)
	first_name			= models.CharField(max_length=50)
	last_name			= models.CharField(max_length=50)
	source				= models.CharField(max_length=50)
	
	created				= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True,auto_now_add=True)
	
class Invitation(models.Model):
	sender				= models.ForeignKey('members.User')
	prospect			= models.ForeignKey('members.Prospect')
	curl				= models.CharField(max_length=40)

	created				= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True,auto_now_add=True)	
	
	status				= models.CharField(max_length=10, default='SENT',choices=settings.ENUMS["INV_STATES"])
	
	def create_curl(self):
		p = self.prospect
		cid = UserManager().make_random_password(5)
		self.curl = cid
	
	def sendmail(self):
		link = 'http://dev.spiffcity.com/members/i/'+self.curl+"/"+self.prospect.first_name+"/"+self.prospect.last_name+"/"
		link = link.strip("/")
		
		message = """%s thinks you should join Spiff City!\nA personal message from Russell:\nHey, have you checked out Spiff City? Get great deals and get rewarded for all your Social activity.  Spiff City is fun, dynamic, and is changing the rules for getting the best deals and staying in touch with yur social network.  Check it out today!  Just click on this link to sign up:\n%s\n You'll immediately get started earning your Spiff City points automatically!  (wahoo!)""" % (self.sender.username , link)

	
		send_mail('Spiffcity Invitation', message , 'webmaster@spiffcity.com',
    [self.prospect.email], fail_silently=True)
	
	
try:
	admin.site.register(ConfigType)
	admin.site.register(User)	
except:
	pass
