from affiliate.comission import CJ
from libs.utils import ValueManager
from apps.spiffs.models import Deal
from apps.core.models import Category
from django.http import HttpResponse

#from apps.importer.affiliate.groupon import GrouponDeal

import simplejson as json
import datetime
import settings

def index(request):
	pass
	
def approval_list(request):
	pass
	
def approve(request):
	pass
	
def import_gp_deals(request):
    devision_id = 'new-york'
    gd = GrouponDeal(settings.CRED["GROUPON_DEAL_URL"],devision_id,settings.CRED["GROUPON_CLIENT_ID"])
    return HttpResponse(gd.make_groupon_deals())


def import_deals (request):
	results = CJ.get_deals()
	results	= ValueManager.translate_bytes(results)
	results = json.loads(results)
	
	if results['count'] > 0:
		products = results['products']['Product']
		for product in products:
			try:
				dealOnep = datetime.datetime.now() 

				dealClose =datetime.datetime(dealOnep.year,int(dealOnep.month)+2, dealOnep.day, dealOnep.hour, dealOnep.minute, dealOnep.second, dealOnep.microsecond)

				dealExp = datetime.datetime(dealOnep.year,int(dealOnep.month)+4, dealOnep.day, dealOnep.hour, dealOnep.minute, dealOnep.second, dealOnep.microsecond)

				deal = Deal(
							title			= product['name'],
							description		= product['description'],
							category		= Category.objects.get(id=1),
							image_url		= product['imageUrl'],

							deal_id 		= product['adId'],
							advertiser_name	= product['advertiserName'],
							manufacturer_name=product['manufacturerName'],

							price			= product['salePrice'],
							value			= product['price'],
							currency		= product['currency'],

							deal_open		= dealOnep,
							deal_close		= dealClose,
							expiration_date	= dealExp,

							sku				= product['sku'],
							upc				= product['upc'],
							catalog_id		=product['catalogId'],

							purchase_url	= product['buyUrl'],

							is_free			= False,
							is_featured		= False
					)
				deal.save()
			except Exception,ex:
				return HttpResponse(ex)
				
                
	return HttpResponse("done")
