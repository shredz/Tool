
import urllib,simplejson,urllib2
import datetime
from xml.dom import minidom

from apps.importer.groupon.models import *

class GrouponDeal:
    def __init__(self,url,devision_id,client_id):
        self.url = url
        self.devisionId = devision_id
        self.clientId = client_id
        
    def get_deals(self):
        request_url = self.url+'?division_id='+self.devisionId+'&client_id='+self.clientId
        response = urllib.urlopen(request_url)
        return response
    def get_location(self, obj):
        location =None
        try:
            location = Gp_Location.objects.get(latitude=str(obj['lat']),longitude=str(obj['lng']))
        except Gp_Location.DoesNotExist:
            location = Gp_Location(latitude=str(obj['lat']),longitude=str(obj['lng']),location_name=obj['name'],timezone=obj['timezone'],location_id=obj['id'])
            location.save()
        return location
    def get_address(self, obj,location):
        address =None
        try:
            address = Gp_Address.objects.get(city=obj[0]['city'],state =obj[0]['state'],zipcode=obj[0]['postalCode'],phonenumber=obj[0]['phoneNumber'])
        except Gp_Address.DoesNotExist: 
            address = Gp_Address(city=obj[0]['city'],state =obj[0]['state'],zipcode=obj[0]['postalCode'],phonenumber=obj[0]['phoneNumber'],street_line_1=obj[0]['streetAddress1'],street_line_2=obj[0]['streetAddress2'],country=Gp_Country.objects.get(id=1),location=location)
            address.save()
        return address
    def get_merchant(self, merchant):
        result =None
        try:
            result = Gp_Merchant.objects.get(merchant_id=merchant['id'],name=merchant['name'])
        except Gp_Merchant.DoesNotExist:
             result = Gp_Merchant(merchant_id=merchant['id'],name=merchant['name'],websiteUrl=merchant['websiteUrl'])
             result.save()
        return result
    def set_options(self,options,deal):
        for option in options:
            option_obj = Gp_Deal_Options(option_id=option['id'],title=option['title'],buy_url=option['buyUrl'],expiration_date = option['expiresAt'].replace('T',' ').replace('Z',''),price=option['price']['amount'],value=option['value']['amount'],deal=deal)
            option_obj.save()
        return None
    def make_groupon_deals(self):
        deals_info = simplejson.load(self.get_deals())
        list = {} 
        all_deal = []   
        for one in deals_info['deals']:
            start_at =None
            if one['startAt']:
                start_at = one['startAt'].replace('T',' ').replace('Z','')
            end_at=None
            if one['endAt']:
                end_at = one['endAt'].replace('T',' ').replace('Z','')
            title = one ['title']
            deal_id = one['id']
            location = self.get_location(one['division'])
            is_featured = False
            if str(one ['placementPriority']) == 'featured':
                is_featured = True
            image_urls = one['largeImageUrl']
            tags = one['tags']
            purchase_url = one['dealUrl']
            status = one['status']
            totalSold = int(one['soldQuantity'])
            address =None
            if one['options'][0]['redemptionLocations']:
                address = self.get_address(one['options'][0]['redemptionLocations'],location)
            description = one['options'][0]['details'][0]['description']
            currency= one['options'][0]['value']['currencyCode']
            highlights = one['highlightsHtml']
            pitchhtml = one['pitchHtml']
            merchant = self.get_merchant(one['merchant'])
            deal_obj = Gp_Deal(deal_id=deal_id,title=title,status=status,description=description,location=location,address=address,pitchhtml=pitchhtml,deal_open=start_at,deal_close=end_at,total_sold=totalSold,currency=currency,is_featured=is_featured,highlights=highlights,purchase_url=purchase_url,image_urls=image_urls,tags=tags,merchant=merchant)
            try:
                deal_obj.save()
                self.set_options(one ['options'],deal_obj)
            except Exception ,e:
                pass
        return "Done"
