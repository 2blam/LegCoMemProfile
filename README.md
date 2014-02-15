Objective
----------------------------------------------------------------
Use Scrapy to crawl the members of Legislative Council (LegCo) of The Hong Kong Special Adminstrative Region of the People's Republic of China.

Each member profile can be found from this URL:
http://www.legco.gov.hk/general/english/members/yr12-16/biographies.htm

How to Run
----------------------------------------------------------------
scrapy crawl LegCoMemProfileSpider -o legcoMemProfile.json -t json

Unescape unicode in JSON
----------------------------------------------------------------
The output JSON from scrapy, the Chinese characters are encode as \uXXXX.
To generate a readable JSON file, you can run the unescapeUnicodeInJSON.py in scripts folder

Requirements
----------------------------------------------------------------
- Python 2.7.6 or above
- Scrapy 0.20.2 or above
- Pillow 2.3.0 or above

Update
----------------------------------------------------------------
Date: 2 Feb 2014
unescapeUnicodeInJSON.py added

Date: 21 Jan 2014
Spider updated. It can now crawl the Chinese profile information

Other
----------------------------------------------------------------
<s>At the moment the Chinese is encoded as unicode (saved as \uXXXX). </s>

<s>It may introduce problem for text searching. </s>

<s>It needs to further investigate</s>

It was fixed by running unescapeUnicodeInJSON.py 