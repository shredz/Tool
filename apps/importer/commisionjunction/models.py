from django.db import models


from apps.spiffs.models import Deal

class CDealManager (models.Manager):
	def list_page (self, page , total):
		return CDeal.objects.filter(approved=True).extra(order_by=['id'])[(page-1)*total:(page*total)]

class CDeal(Deal):
	isbn				= models.CharField(max_length=30)
	m_sku				= models.CharField(max_length=30)
	upc 				= models.CharField(max_length=50)
	
	retailprice			= models.DecimalField(max_digits=10, decimal_places=2)
	manufacturer_name	= models.CharField(max_length=200)
	
	price_amount		= models.DecimalField(max_digits=10, decimal_places=2)
	catalog_id			= models.CharField(max_length=30)
	
	objects				= CDealManager()
	
	"""    
    sku  :  J16076
	advertiserId  :  2637628
	isbn  :  #
	manufacturerSku  :  #
	buyUrl  :  http://www.kqzyfj.com/click-5377414-10669980?url=http%3A%2F%2Fwww.reebok.com%2FDE%2Fproduct%3FmodelId%3DZZ216%26articleId%3DJ16076&cjsku=J16076
	description  :  Reif f&#0252;r die Zukunft bist du mit dem Pump Vintage Mid. Die Pump-Technologie bietet damals wie heute eine individuelle Passform und das moderne, mittelhohe Skater-Profil ist perfekt geeignet f&#0252;r Ramp und Stra&#0223;e. Teil der Emporio Armani / Reebok Kollektion.
	retailPrice  :  0.0 #
	upc  :  #
	manufacturerName  :  Reebok#
	advertiserName  :  Reebok - DE
	currency  :  USD
	adId  :  10669980
	salePrice  :  169.95
	inStock  :  #
	price  :  169.95
	catalogId  :  cjo:220#
	imageUrl  :  http://static.reebok.com/images/fluid/customers/c483/ZZ216/ZZ216_clickpan/main_variation_J16076_view_FRONT_306x333.jpg
	name  :  Der Pump Vintage Mid
	"""

    
	def __unicode__(self):
		return self.title

