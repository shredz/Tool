
import urllib,simplejson,urllib2
import datetime
from xml.dom import minidom

from apps.importer.linkshare.models import *
from apps.core.models import Category

class LS:
    def __init__(self,url,token,keyword,advertiserId):
        self.url = url
        self.token = token
        self.keyword = keyword
        self.advertiserId = advertiserId
    
    def get_deals(self, pagenumber):
        request_url = self.url+'token='+self.token+'&keyword='+self.keyword+'&mid='+self.advertiserId+'&max=100&sort=retailprice&sorttype=asc&pagenumber='+str(pagenumber)
        response = urllib.urlopen(request_url)
        return response
        
    def make_cats(self, obj):
        parent = Category.objects.get(id=1)
        
        try:
            primary = Category.objects.get(title=obj['primary'])
        except Category.DoesNotExist:
            primary = Category(title=obj['primary'], parent=parent)
            primary.save()
        try: 
            cat = Category.objects.get(title=obj['secondary'], parent=primary)
        except Category.DoesNotExist:
            cat = Category(title=obj['secondary'], parent=primary)
            cat.save()
        return cat
        
    def make_deal_page(self, page):
        dom = minidom.parse(self.get_deals(page))
        for dom_deal in dom.getElementsByTagName('item'):
            deal = LDeal()

            for field in dom_deal.childNodes:
                field_name = field.tagName
                if field_name == "category":
                    cats = {}
                    for cat in field.childNodes:
                        cats[cat.tagName] = cat.childNodes[0].data
                    deal.category = self.make_cats(cats)
                    
                elif field_name == "description":
                    desc = {}
                    for des in field.childNodes:
                        desc[des.tagName] = des.childNodes[0].data
                        
                    deal.description = desc['long']
                    deal.description_short = desc['short']
                    
                elif field_name == "price":
                
                    deal.price = field.childNodes[0].data
                    deal.currency = field.attributes['currency'].value
                
                elif field_name == "createdon":
                    deal.deal_open = field.childNodes[0].data.replace('/',' ')
                
                elif field_name == "linkurl":
                    deal.purchase_url = field.childNodes[0].data
                
                elif field_name == "imageurl":
                    deal.image_url = field.childNodes[0].data
                
                elif field_name == "mid":
                    deal.mid = field.childNodes[0].data
                    
                elif field_name == "merchantname":
                    deal.advertiser_name = field.childNodes[0].data
                
                elif field_name == "linkid":
                    deal.deal_id = field.childNodes[0].data
                
                elif field_name == "sku":
                    deal.sku = field.childNodes[0].data
                
                elif field_name == "productname":
                    deal.title = field.childNodes[0].data
            
            deal.save()
        return dom
		
    def make_deals(self):
        dom = self.make_deal_page(1)
        
        for nofPages in dom.getElementsByTagName('TotalPages'):
            total_pages = int(nofPages.childNodes[0].data)
        
        for page in range(1,total_pages):
            self.make_deal_page(page)

