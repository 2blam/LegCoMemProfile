# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LegcomemprofileItem(Item):
    name = Field()
    area = Field()
    constituency = Field()
    edu_prof = Field()
    occupation = Field()
    affiliation = Field()
    office_address = Field()
    office_telephone = Field()
    office_fax = Field()
    email = Field()
    homepage = Field()
    #for download images ** field names (image_urls, images) are fixed
    image_urls = Field()
    images = Field()