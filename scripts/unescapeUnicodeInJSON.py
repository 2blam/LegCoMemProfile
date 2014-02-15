import json

outputfn = 'legcoMemProfile_unescape.json'

json_data = open('legcoMemProfile.json')
data = json.load(json_data)
json_data.close()


# output the file in utf-8, but maintain the Chinese characters
s = json.dumps(data, indent=2, ensure_ascii=False)
open(outputfn, 'w+').write(s.encode('utf-8'))