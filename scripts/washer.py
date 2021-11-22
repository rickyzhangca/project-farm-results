
import json


with open('scripts/scraped.json') as f:
  scraped = json.load(f)
  
washed = scraped
for video in scraped:
    video.pop('subtitles', None)
    video.pop('comments', None)
    video.pop('numberOfSubscribers', None)
    video.pop('channelUrl', None)
    video.pop('channelName', None)
    video.pop('duration', None)
    video.pop('details', None)
    video['date'] = video['date'][:10]

json_object = json.dumps(washed, indent = 4, ensure_ascii=False) 
with open("scripts/washed.json", "w") as outfile: 
    outfile.write(json_object) 