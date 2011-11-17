from django.db import models
from django.contrib import admin

import settings

#from apps.core import models

class Account(models.Model):
	uid					= models.PositiveIntegerField()
	oauth_token			= models.CharField(max_length=255, null=True)
	oauth_token_secret	= models.CharField(max_length=255, null=True)
	other_data			= models.TextField(null=True)
	
	spiffuser			= models.ForeignKey('members.User')
	account_type		= models.CharField(max_length=20,choices=settings.ENUMS['NETWORKS'])

	@staticmethod
	def get_for_user(user,_type='facebook'):
		try:
			return Account.objects.get(spiffuser=user,account_type=_type)
		except:
			return None

admin.site.register(Account)

"""
class Community(core_models.DisplayObject):
	members				= models.ManyToManyField('members.User')

class Forum(core_models.DisplayObject):
	community 			= models.ForeignKey('social.Community')
	
class Discussion(core_models.DisplayObject):
	pass

class ForumDiscussion(Discussion):
	forum 				= models.ForeignKey('social.Forum')

class SpiffDiscussion(Discussion):
	spiffobject			= models.ForeignKey('core.SpiffObject')

class Comment (models.Model):
	discussion			= models.ForeignKey('social.Discussion')
	user				= models.ForeignKey('members.User')
	replyto				= models.ForeignKey('self',null=True)
	content				= models.CharField(max_length=255)
	likes				= models.PositiveIntegerField(max_length=5)
	dislikes			= models.PositiveIntegerField(max_length=5)
"""
