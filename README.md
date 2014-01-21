Objective
----------------------------------------------------------------
Use Scrapy to crawl the members of Legislative Council (LegCo) of The Hong Kong Special Adminstrative Region of the People's Republic of China.

Each member profile can be found from this URL:
http://www.legco.gov.hk/general/english/members/yr12-16/biographies.htm

How to Run
----------------------------------------------------------------
scrapy crawl LegCoMemProfileSpider -o legcoMemProfile.json -t json

Requirements
----------------------------------------------------------------
- Python 2.7.6 or above
- Scrapy 0.20.2 or above
- Pillow 2.3.0 or above

Update
----------------------------------------------------------------
Date: 21 Jan 2014
Spider updated. It can now crawl the Chinese profile information

Other
----------------------------------------------------------------
At the moment the Chinese is encoded as unicode (saved as \uXXXX).
It may introduce problem for text searching. 
It needs to further investigate.