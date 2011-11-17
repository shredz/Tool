def index(request):
	pass

from apps.spiffs.models import *
from apps.members.models import *
from apps.importer.commisionjunction.models import CDeal
from apps.importer.linkshare.models import LDeal
from apps.core.models import *


from libs.utils import Response
from django.views.decorators.csrf import csrf_exempt

from decimal import *


def front_page (request, layout , deal_type , page):
	now = datetime.datetime.now()
	layout = str(layout)
	
	if layout == "0":
		total = 10
		names = ["deal1" ,"deal2" ,"deal3" ,"deal4" ,"deal5" ,"deal6" ,"deal7" ,"deal8" ,"deal9" ,"deal10" ]
	
	if layout == "1":
		total = 4
		names = ["deal1","deal2","deal3","deal4"]	
	
	elif layout == "2":
		total = 8
		names = ["deal1","deal2","deal3","deal7","deal8", "deal4","deal6","deal5"]
		
	elif layout == "3":
		total = 8
		names = ["deal1","deal2","deal3","deal4","deal5","deal6","deal7","deal8"]
	
	"""
	TRACKING = ""
	
	if deal_type == "CJ":
		D = CDeal
		TRACKING = "&sid=%s" % (request.user.id)
		
	elif deal_type == "LS":
		D = LDeal
		TRACKING = "&u1=%s" % (request.user.id)
	
	else:
		D = Deal
		TRACKING = "&u1=%s&sid=%s" % (request.user.id, request.user.id)
		
	"""
	D = CDeal #SWITCH
	deals = D.objects.list_page(page , total)
	
	ds = {}
	count = 0
	
	for deal in deals:
		deal.link = "/spiffs/deal/%s/%s/" % (deal_type , deal.id)
		deal.purchase_url = "/spiffs/v/%s/%s/" % (deal_type, deal.id)
		
		ds[names[count]] = deal
		count = count + 1
	
	return (ds,names)
	
			
def deals (request,page):
	if request.user.is_authenticated():
		user = User.instance(request.user)
		layout = user.get_config("Layout").value
	else:
		layout = 0
	
	deals, names = front_page(request, layout, "CJ" , int(page))	
	
	#return Response.html(len(deals))
	if len(deals) == 0:
		return Response.html("<!-- END -->")
	
	params = {'deals' :  deals , "names" : names,"layout":layout}
	return Response.render("spiffs/schemes/"+str(layout)+".html" , params,request)

def deallist (request,page):
	if request.user.is_authenticated():
		user = User.instance(request.user)
		layout = user.get_config("Layout").value
	else:
		layout = 0
	
	deals, names = front_page(request, layout, "CJ" , int(page))	
	
	#return Response.html(len(deals))
	if len(deals) == 0:
		return Response.html("<!-- END -->")
	
	params = {'deals' :  deals , "names" : names,"layout":layout}
	return Response.render("spiffs/deallist.html" , params,request)
	

def visited(request, deal_type ,deal_id):
	if request.user.is_authenticated():
		uid = request.user.id
	else:
		uid = "0"
	
	
	deal = Deal.objects.get(id=deal_id)
	dv = DealVisit(
		user 	= uid,
		deal_id = deal_id
	)
	dv.save()
	
	if deal_type == "CJ":
		TRACKING = "&sid=%s" % (dv.id)
	elif deal_type == "LS":
		TRACKING = "&u1=%s" % (dv.id)		
	else:
		TRACKING = "&u1=%s&sid=%s" % (dv.id, dv.id)
		
	return Response.send_to(deal.purchase_url+TRACKING)
	


def deal(request,deal_type,deal_id):
	try:
		if deal_type == "CJ":
			deal = CDeal.objects.get(id=deal_id)
			#TRACKING = "&sid=%s" % (request.user.id)
			
		elif deal_type == "LS":
			deal = LDeal.objects.get(id=deal_id)
			#TRACKING = "&u1=%s" % (request.user.id)
			
		else:
			deal = Deal.objects.get(id=deal_id)
			#TRACKING = "&u1=%s&sid=%s" % (request.user.id, request.user.id)
		
		
		deal.purchase_url  = "/spiffs/v/%s/%s/" % (deal_type, deal.id)
		deal.link = "http://dev.spiffcity.com/spiffs/deal/%s/%s/" % (deal_type, deal.id)
		return Response.render("spiffs/deal.html",{"deal":deal},request)
		
	except Deal.DoesNotExist, dne :
		Response.not_found()

def new_deals(request,page):	
	new_deals	 = Deal.objects.list_new(int(page) , 20)
	
	left = new_deals[0:10]
	right = new_deals[10:20]
	
	#Response.html(len(new))
	
	return Response.render("spiffs/new_deals.html" , {"deals": [left , right] , "page" : page , "nextpage" : int(page) + 1 },request)

def gmap(request,page):	
	catgs = Category.objects.values('title').filter(parent='15').distinct()
	return Response.render("spiffs/gmap.html" , {'catgs': catgs},request)

def show_deal(request,page):	
	catgs = Category.objects.values('title').filter(parent=page).distinct()
	return Response.render("spiffs/show_deal.html" , {'catgs': catgs},request)
	
def approve_deal(request, deal_id):
	deal = Deal.objects.get(id=deal_id)
	deal.approved = True
	deal.save()
	
	return Response.json({"success" : True , "message" : "Deal Has Been Approved"})
	
def reject_deal(request , deal_id):
	deal = Deal.objects.get(id=deal_id)
	deal.delete()
	
	return Response.json({"success" : True , "message" : "Deal Has Been DELETED"})
	
@csrf_exempt
def search(request):
	if request.method == "POST":
		keyword = request.POST['str']
		params = {'deals' : Deal.search(keyword) }
		return Response.render("spiffs/deals.html" , params,request)
		
