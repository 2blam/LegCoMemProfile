# -*- coding: utf-8 -*- 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from LegCoMemProfile.items import LegcomemprofileItem
from scrapy.http.request import Request
import datetime
import urllib2
import unicodedata
import time
import re
from urlparse import urljoin

import sys

class MySpider(BaseSpider):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    name = "LegCoMemProfileSpider" #identifer that called from command
    allowed_domains = ["legco.gov.hk"]
    start_urls = ["http://www.legco.gov.hk/general/english/members/yr12-16/biographies.htm"]
    allLinks = []

    def striphtml(data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)

    def parse(self, response):
        # image url prefix 
        image_url_prefix = "http://www.legco.gov.hk"
        # legco member detail url prefix
        member_detail_url_prefix = "http://www.legco.gov.hk/general/english/members/yr12-16/"
        member_detail_url_prefix_ZH = "http://www.legco.gov.hk/general/chinese/members/yr12-16/"

        biographies_url_ZH = "http://www.legco.gov.hk/general/chinese/members/yr12-16/biographies.htm"
        # sleep time
        sleepTime = 0

        #get the Chinese Biographies content
        while True:
                time.sleep(sleepTime)
                 
                hxsBiographies_ZH = HtmlXPathSelector(text=urllib2.urlopen(biographies_url_ZH).read())                
                
                #select related elements
                bio_member_names_ZH = hxsBiographies_ZH.select("//div[@class='bio-member-detail-1']/strong/a/text()").extract()
                bio_member_desc_ZH = hxsBiographies_ZH.select("//div[@class='size2 bio-member-detail-2']/text()").extract()
                

                #print "detailsInfo: ", len(detailsInfo)
                if len (bio_member_names_ZH) == 0:
                    print "Re-request"
                    continue
                else:
                    break

        #request the html content
        hxs = HtmlXPathSelector(response)

        #select related elements
        bio_member_names = hxs.select("//div[@class='bio-member-detail-1']/strong/a/text()").extract()
        bio_member_desc = hxs.select("//div[@class='size2 bio-member-detail-2']/text()").extract()
        bio_member_image_urls = hxs.select("//div[@class='bio-member-photo']/img/@src").extract()
        bio_member_detail_urls = hxs.select("//div[@class='bio-member-detail-1']/strong/a/@href").extract()

        items = []
        
        #for each member
        #for idx in range(1):
        for idx in range(len(bio_member_names)):        
            item = LegcomemprofileItem()

            name = bio_member_names[idx]
            desc = bio_member_desc[idx]

            name_ZH = bio_member_names_ZH[idx]
            desc_ZH = bio_member_desc_ZH[idx]

            #constituency: (New Territories West+)
            #(1) remove whitespace
            #(2) remove open and close brace
            #(3) replace 
            #    * : Functional Constituency
            #    + : Geographical Constituency
            area = desc.strip()[1:-1]

            if area[-1] == "*":
                constituency = "Functional Constituency" 
                constituency_ZH = "功能界別"  
            else:
                constituency = "Geographical Constituency"
                constituency_ZH = "地方選區"
            
            #remove * or +
            area = area[:-1]
            area_ZH = (desc.strip()[1:-1])[:-1]
            
            image_urls = [urljoin(image_url_prefix, bio_member_image_urls[idx])]
            
            #go to the child page
            member_detail_url = member_detail_url_prefix + bio_member_detail_urls[idx]
            #print "-----------------",member_detail_url
            while True:
                time.sleep(sleepTime)
                hxsResultDetail = HtmlXPathSelector(text=urllib2.urlopen(member_detail_url).read())                
                
                #get the details information
                detailsInfo = hxsResultDetail.select("//div[@id='container']/div/ul").extract()
                contactInfo = hxsResultDetail.select("//div[@class='table_overflow']/table/tr/td[@valign='top']").extract()

                #print "detailsInfo: ", len(detailsInfo)
                if len (detailsInfo) == 0:
                    print "Re-request"
                    continue
                else:
                    break

            #Education and professional qualifications
            edu_prof = detailsInfo[1]              
            edu_prof  = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(edu_prof)

            #Occupation :
            occupation = detailsInfo[2]
            occupation = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(occupation)            


            #Political affiliation :
            if len(detailsInfo) == 3: # handle "-" situation 
                affiliation = "-"
            else:
                affiliation = detailsInfo[3]            
                affiliation = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(affiliation)            
            
            TAG_RE = re.compile(r'<[^>]+>')
            CTR_RE = re.compile(r'[\n\r\t]')
            
            office_address =TAG_RE.sub('', contactInfo[2])
            office_address = CTR_RE.sub('', office_address)

            office_telephone = TAG_RE.sub('', contactInfo[5])            
            office_telephone = CTR_RE.sub('', office_telephone)
            
            office_fax = TAG_RE.sub('', contactInfo[8])
            office_fax = CTR_RE.sub('', office_fax)

            email =  TAG_RE.sub('', contactInfo[11])
            email = CTR_RE.sub('', email)

            homepage = TAG_RE.sub('', contactInfo[14])
            homepage = CTR_RE.sub('', homepage)

            #go to the chinese child page
            member_detail_url = member_detail_url_prefix_ZH + bio_member_detail_urls[idx]
            #print "-----------------",member_detail_url
            while True:
                time.sleep(sleepTime)
                hxsResultDetail = HtmlXPathSelector(text=urllib2.urlopen(member_detail_url).read())                
                
                #get the details information
                detailsInfo_ZH = hxsResultDetail.select("//div[@id='container']/div/ul").extract()
                contactInfo_ZH = hxsResultDetail.select("//div[@class='table_overflow']/table/tr/td[@valign='top']").extract()

                #print "detailsInfo_ZH: ", len(detailsInfo_ZH)
                if len (detailsInfo_ZH) == 0:
                    print "Re-request"
                    continue
                else:
                    break

            #Education and professional qualifications
            edu_prof_ZH = detailsInfo_ZH[1]              
            edu_prof_ZH  = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(edu_prof_ZH)

            #Occupation :
            occupation_ZH = detailsInfo_ZH[2]
            occupation_ZH = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(occupation_ZH)            


            #Political affiliation :
            if len(detailsInfo_ZH) == 3: # handle "-" situation 
                affiliation_ZH = "-"
            else:
                affiliation_ZH = detailsInfo_ZH[3]            
                affiliation_ZH = re.compile('<li>(.*?)</li>', re.DOTALL |  re.IGNORECASE).findall(affiliation_ZH)            
            
            office_address_ZH =TAG_RE.sub('', contactInfo_ZH[2])
            office_address_ZH = CTR_RE.sub('', office_address_ZH)

            item["name"] = name
            item["name_ZH"] = name_ZH
            item["area"] = area
            item["area_ZH"] = area_ZH
            item["constituency"] = constituency
            item["constituency_ZH"] = constituency_ZH            
            item["edu_prof"] = edu_prof            
            item["edu_prof_ZH"] = edu_prof_ZH
            item["occupation"] = occupation
            item["occupation_ZH"] = occupation_ZH
            item["affiliation"] = affiliation
            item["affiliation_ZH"] = affiliation_ZH
            item["office_address"] = office_address
            item["office_address_ZH"] = office_address_ZH
            item["office_telephone"] = office_telephone            
            item["office_fax"] = office_fax
            item["email"] = email
            item["homepage"] = homepage
            item["image_urls"] = image_urls

            items.append(item)
        
        return items
        
 