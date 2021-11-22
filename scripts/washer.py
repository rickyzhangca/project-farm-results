
import json
import os


with open('scripts/scraped.json') as f:
  scraped = json.load(f)

washed = []

nontesting = ['Kt_TSQXkaNM', 'HVzGRgBgUq0', 'NwIjLECJmA8', 'JzbU4LdgZpI', 'ajx0JD-caBA', '-DgzhVkAIuc', 'VwePft315Ds', 'wT0TTGO2CUY', '2ySSEzqEa_k', 'w9fTKZN0Eps', 'vVyin2n24X8', 'uzMGbxE_PZU', 'YeFat4aMcYg', 'ikAQdpUfVlI', 'vv1w9N9v3SA', '7oLHtW2psbA', 'QIeEU6Ta1Hc', 'PORwOE4B0GA', 'kZ0l4pkfP4Y', 'W5IJfrXH1lE', 'QrxsCKMTqHI', 'agAWXnT4-EQ', 'yIypt2-xlCY', 'Y_qx6TiDnmg']

for video in scraped:
    if video['id'] in nontesting:
        continue
    video.pop('subtitles', None)
    video.pop('comments', None)
    video.pop('numberOfSubscribers', None)
    video.pop('channelUrl', None)
    video.pop('channelName', None)
    video.pop('duration', None)
    video.pop('details', None)
    video['date'] = video['date'][:10]
    video['title'] = video['title'].replace('&amp;', '')
    video['title'] = video['title'].replace('/', '|')
    video['category'] = '_placeholder'
    washed.append(video)

json_object = json.dumps(washed, indent = 4, ensure_ascii=False) 
with open("scripts/washed.json", "w") as outfile: 
    outfile.write(json_object) 

class front_matter:
    _content = {}
    def __init__(self) -> None:
        pass
    def add(self, variable, value):
        self._content[variable] = value
    def assemble(self):
        assembled = '---\n'
        for key, value in self._content.items():
            if key == 'title':
                # assembled += key + ": '" + value + "'" + '\n'
                assembled += 'temp'
                continue
            assembled += key + ': ' + value + '\n'
        assembled += '---\n'
        return assembled

for video in washed:
    with open('_posts/' + video['date'] + '-' + video['title'] + '.md', "w") as outfile: 
        header = front_matter()
        header.add('layout', 'post')
        header.add('title', video['title'])
        header.add('date', video['date'])
        header.add('youtube', video['url'])
        header.add('category', video['category'])
        outfile.write(header.assemble() + 'test content') 