# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LegcomemprofileItem(Item):
    name = Field()
    name_ZH = Field()
    area = Field()
    area_ZH = Field()
    constituency = Field()
    constituency_ZH = Field()
    edu_prof = Field()
    edu_prof_ZH = Field()
    occupation = Field()
    occupation_ZH = Field()
    affiliation = Field()
    affiliation_ZH = Field()
    office_address = Field()
    office_address_ZH = Field()
    office_telephone = Field()
    office_fax = Field()
    email = Field()
    homepage = Field()
    #for download images ** field names (image_urls, images) are fixed
    image_urls = Field()
    images = Field()