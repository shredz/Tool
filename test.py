import os,sys,settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


if 	 sys.argv[1] == "TESTIMPORT":
	pass

elif sys.argv[1] == "CJREPORTS":
	from apps.importer.commisionjunction import CJ
	#CJ ().make_reports()get_reports
	print CJ ().make_reports()
	
	

elif sys.argv[1] == "ADDHOST":
	from apps.security.models import AllowedHosts
	AllowedHosts(ip=sys.argv[2]).save()
	
elif   sys.argv[1] == "IMPORTCJ":
	from apps.importer.commisionjunction import CJ
	print CJ ().make_deals()
	
elif sys.argv[1] == "LISTCJ":
	from apps.importer.commisionjunction.models import CDeal
	for deal in CDeal.objects.all():
		#same_image 	= CDeal.objects.filter(image_url=deal.image_url).count()
		#same_url 	= CDeal.objects.filter(purchase_url=deal.purchase_url).count()
		
		print deal.id , " : ",deal.deal_id 

elif sys.argv[1] == "LISTNEW":
	from apps.spiffs.models import Deal
	deals = Deal.objects.list_new(1,10)
	for deal in deals:
		print deal.id , " : ", deal.image_url

elif sys.argv[1] == "IMPORTLS":
	#2- IMPORT LS DEALS
	from apps.importer.linkshare import LS
	url 		= settings.CRED['LINKSHARE_URL']
	token 		= settings.CRED['LINKSHARE_TOKEN']
	keyword 	= 'Deal'
	advertiserId= '36553'

	ls = LS(url,token,keyword,advertiserId)
	res = ls.make_deals()
	print "LS : ",res

elif sys.argv[1] == "DELETEDEALS":
	from apps.importer.linkshare.models import LDeal
	for deal in LDeal.objects.all():
		deal.delete()
		print "LDEAL : ",deal.id,"deleted"
		
	from apps.importer.commisionjunction.models import CDeal
	for deal in CDeal.objects.all():
		deal.delete()
		print "CDEAL : ",deal.id,"deleted"
	
	from apps.spiffs.models import Deal
	for deal in Deal.objects.all():
		deal.delete()
		print "DEAL : ",deal.id,"deleted"
	
	from apps.core.models import SpiffObject
	for deal in SpiffObject.objects.all():
		deal.delete()
		print "SpiffObject : ",deal.id,"deleted"
	
