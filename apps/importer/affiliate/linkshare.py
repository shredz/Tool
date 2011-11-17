
import urllib,simplejson,urllib2
import datetime
from xml.dom import minidom

from apps.importer.linkshare.models import *

class LinkShareDeal:
    def __init__(self,url,token,keyword,advertiserId):
        self.url = url
        self.token = token
        self.keyword = keyword
        self.advertiserId = advertiserId
    def get_deals(self, pagenumber):
        request_url = self.url+'token='+self.token+'&keyword='+self.keyword+'&mid='+self.advertiserId+'&max=100&sort=retailprice&sorttype=asc&pagenumber='+str(pagenumber)
        response = urllib.urlopen(request_url)
        return response
    def set_linkshare_cat(self, obj):
        cat=primary=None
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
    def set_linkshare_desc(self,obj):
        description = None
        try:
            description = Ls_Description.objects.get(short=obj['short'], long=obj['long'])
        except Ls_Description.DoesNotExist:
            description = Ls_Description(short=obj['short'], long=obj['long'])
            description.save()
        return description
    def add_linkshare_deals(self,obj):
        try:
            Ls_Deal.objects.get(url=obj['linkurl'])
        except Ls_Deal.DoesNotExist:
            linkshare_cat = self.set_linkshare_cat(obj['category'])
            linkshare_desc = self.set_linkshare_desc(obj['description'])
            dealOnep = datetime.datetime.now() 
            dealClose =datetime.datetime(dealOnep.year,int(dealOnep.month)+2,dealOnep.day,dealOnep.hour,dealOnep.minute,dealOnep.second,dealOnep.microsecond)
            lsdeal_obj = Ls_Deal(url=obj['linkurl'],description=linkshare_desc,category=linkshare_cat,started_on=obj['createdon'].replace('/',' '),end_on=dealClose,linkid=obj['linkid'],picture_url=obj['imageurl'],mid=obj['mid'],merchantname =obj['merchantname'],productname=obj['productname'],sku=obj['sku'],price=obj['price'], currency=obj['currency'])
            lsdeal_obj.save()
        return None
    def make_dom_deal(self, dom):
        for deal in dom.getElementsByTagName('item'):
            Deal = {}
            for field in deal.childNodes:
                field_name = field.tagName
                if field_name == "category":
                    cats = {}
                    for cat in field.childNodes:
                        cats[cat.tagName] = cat.childNodes[0].data
                    Deal[field_name] = cats
                elif field_name == "description":
                    desc = {}
                    for des in field.childNodes:
                        desc[des.tagName] = des.childNodes[0].data
                    Deal[field_name] = desc
                elif field_name == "price":
                    Deal[field_name] = field.childNodes[0].data
                    Deal['currency'] = field.attributes['currency'].value
                elif field_name == "createdon":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "linkurl":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "imageurl":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "mid":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "merchantname":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "linkid":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "sku":
                    Deal[field_name] = field.childNodes[0].data
                elif field_name == "productname":
                    Deal[field_name] = field.childNodes[0].data
            self.add_linkshare_deals(Deal)
        return None
    def make_linkshare_deals(self):
        dom =None 
        pageNumber = 1
        linkShare_res = self.get_deals(pageNumber)
        dom =minidom.parse(linkShare_res)
        total_pages = 1
        for nofPages in dom.getElementsByTagName('TotalPages'):
            total_pages = int(nofPages.childNodes[0].data)
        if total_pages >= pageNumber:
            for page in range(total_pages):
                if dom != None:
                    dom = self.make_dom_deal(dom)
                elif dom == None:
                    linkShare_res = self.get_deals(pageNumber+page)
                    dom =minidom.parse(linkShare_res)
                    dom = self.make_dom_deal(dom)
        return 'Done'
