# Scrapy settings for LegCoMemProfile project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'LegCoMemProfile'

SPIDER_MODULES = ['LegCoMemProfile.spiders']
NEWSPIDER_MODULE = 'LegCoMemProfile.spiders'

#enable images pipeline
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE= 'C:/[DATA]/code4hk/LegCoMemProfile/profile_image/'