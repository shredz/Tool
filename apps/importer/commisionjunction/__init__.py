import settings

from libs.utils import ValueManager

from apps.importer.commisionjunction.models import CDeal
from apps.core.models import Category
from apps.reporting.models import Report
from apps.members.models import User
from apps.spiffs.models import ActivityType, SpiffActivity, UserDeal

import subprocess
import simplejson as json

class CJ:
	def __init__(self):
		pass
	
	def get_daily_reports (self, date):
		dateType = "posting"
		advertiserIds = ""
		websiteIds = ""
		actionStatus = "all" #all, new, extended, closed, locked
		actionTypes = "sale" #bonus, click, impression, sale, lead, advanced sale, advanced lead, performance incentive
		adIds = ""
		countries = ""
		correctionStatus= ""
		sortBy ="" #actionStatus,actionType,adId,advertiserId,advertiserName,commissionAmount,
		#country,eventDate,orginal,originalActionId,postingDate,sId,saleAmount,websiteId
		sortOrder = "asc"

		command = [
					r"perl", 
					settings.CJPERL+"CJ_DailyPublisherCommissionSearch.pl",
					settings.CRED['CJ_KEY'],
					date,
					dateType,
					settings.CRED['CJ_ADVERTISERS'],
					websiteIds,
					actionStatus,
					actionTypes,
					adIds,
					countries,
					correctionStatus,
					sortBy,
					sortOrder
				]
		
		print command
		results = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
		print results
		return results[0]
	
	
	def get_reports(self):
		realtimeCommissionService_res = subprocess.Popen([r"perl", settings.CJPERL+"realtimeCommissionService.pl"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

		return realtimeCommissionService_res[0]
        
		#return subprocess.Popen([r"perl", settings.CJPERL+"CJ_CommissionService.pl"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
		data = [
			{
				'adId' :'',
				'advertiserId' :'',
				'advertiserName':'',
				'commissionAmount':'',
				'country':'',
				'details_amount' :'',
				'details_commission' :'',
				'details_quantity' :'',
				'details_sku' :'',
				'eventDate' :'',
				'saleAmount' :'',
				'surfer' :'',
				'websiteId' :''
			}
		]
		
		return json.dumps(data)

	def make_spiff_activity(self, report):
		if report:		
			try:
				user = User.objects.get(id=report.visit.user)
				try:
					ud = UserDeal.objects.get(user=user, deal=report.deal)
				except UserDeal.DoesNotExist, dne:
					ud = UserDeal(user=user, deal=report.deal)
					ud.save()
		
				at = ActivityType.objects.get(title="BOUGHT_DEAL")
				sa = SpiffActivity(user=user,activity_type=at,userdeal=ud,points=2)#, report=report)
				sa.save()
				user.award_points(sa)
				
				report.visit.status = "RECEIVED"
				report.visit.save()
			
			except User.DoesNotExist, dne:
				print "the use for specified sid : %s does not exist " % (report.sid)
		else:
			print "Could not award_points"

	def make_reports(self, date = '10/13/2011'):
		
		results	= ValueManager.translate_bytes(self.get_daily_reports(date))
		reports = json.loads(results)
		
		print "totalResults : ", reports["totalResults"]
				
		if reports["totalResults"] == '0':
			print "NO RESULTS FOUND FOR PARTICULAR DATE", date
		elif reports["totalResults"] == '1':
			print "JUST ONE REPORT TODAY"
			rep = Report.create_from_dic (reports["publisherCommissions"]["PublisherCommissionV2"])
			self.make_spiff_activity(rep)
		else:
			print "MORE REPORTS!!"
			
			for report in reports["publisherCommissions"]["PublisherCommissionV2"]:
				rep = Report.create_from_dic (report)
				self.make_spiff_activity(rep)

	def get_deals(self):
		return subprocess.Popen([r"perl", settings.CJPERL+"CJ_GetProducts.pl",settings.CRED['CJ_KEY'],settings.CRED['CJ_WEBSITE_ID'],settings.CRED['CJ_ADVERTISERS']], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
	
	def make_deals(self):
		results	= ValueManager.translate_bytes(self.get_deals())
		results = json.loads(results)
		if results['count'] > 0:
			products = results['products']['Product']
			for product in products:
				deal = CDeal ()
				deal.sku 	=		product['sku']
				deal.mid 	=		product['advertiserId']
				deal.isbn 	=		product['isbn']
				deal.m_sku 	=		product['manufacturerSku']
				deal.purchase_url 	=		product['buyUrl']
				deal.description 	=		product['description']
				deal.retailprice 	=		product['retailPrice']
				deal.upc 	=		product['upc']
				deal.manufacturer_name 	=		product['manufacturerName']
				deal.advertiser_name 	=		product['advertiserName']
				deal.currency 	=		product['currency']
				deal.deal_id 	=		product['adId']
				deal.price_amount 	=		product['salePrice']
				deal.price 	=		product['price']
				deal.catalog_id 	=		product['catalogId']
				deal.image_url 	=		product['imageUrl']
				deal.title 	=		product['name']
				
				deal.category	=	Category.objects.get(id=1)
				try:
					deal.save()
				except Exception, ex:
					print ex.message
					
