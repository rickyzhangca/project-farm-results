
import json

with open('scripts/scraped.json') as f:
  scraped = json.load(f)

washed = []

nontesting = ['S7D_FqpAvpo', 'psd_BYMljpY', 'RqzhmFCTbCA', '0Dv3TTYaWgI', '0x1546Jetjs', 'Hr8jIwVyIFE', 'XnIRdKZId3s', '9eeDAne-X5I', '4cc2JD3loFc', 'IuGWHfWqWtg', 'llQ2SmOML_k', 'OraBMAEF5rs', 'VXIu3oo8z4c', '5H_mZTh5bHY', 'N0gP4aEad-w', 'HNRO48PlbHg', 'prXiQgVVnDY', 'Wmg0bzuO1Mc', 'yt5a1cWd4', '7U26etcwKdU', 'Kt_TSQXkaNM', 'HVzGRgBgUq0', 'NwIjLECJmA8', 'JzbU4LdgZpI', 'ajx0JD-caBA', '-DgzhVkAIuc', 'VwePft315Ds', 'wT0TTGO2CUY', '2ySSEzqEa_k', 'w9fTKZN0Eps', 'vVyin2n24X8', 'uzMGbxE_PZU', 'YeFat4aMcYg', 'ikAQdpUfVlI', 'vv1w9N9v3SA', '7oLHtW2psbA', 'QIeEU6Ta1Hc', 'PORwOE4B0GA', 'kZ0l4pkfP4Y', 'W5IJfrXH1lE', 'QrxsCKMTqHI', 'agAWXnT4-EQ', 'yIypt2-xlCY', 'Y_qx6TiDnmg']

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
with open("scripts/washed_new.json", "w") as outfile: 
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
            if key == 'title' or 'video-title':
                assembled += key + ': "' + value.replace('"', r'\"') + '"' + '\n'
                # assembled += 'temp'
                continue
            assembled += key + ': ' + value + '\n'
        assembled += '---\n'
        return assembled

with open('scripts/washed.json') as f:
  washed = json.load(f)
for video in washed:
    with open('_posts/' + video['date'] + '-' + video['id'] + '.md', "w") as outfile: 
        header = front_matter()
        header.add('layout', 'post')
        header.add('title', video['id'])
        header.add('video-title', video['title'])
        header.add('date', video['date'])
        header.add('youtube', video['url'])
        header.add('category', video['category'])

        r = ''
        badge = ''
        # content
        if video['results'] != []:
            for result in video['results']:
                if result['type'] == 'Winner':
                    badge = '<span class="inline-flex items-center justify-center px-2 py-1 mr-2 text-sm font-semibold leading-none text-red-50 bg-red-600 rounded-full">' + result['type'] + '</span>'
                else:
                    badge = '<span class="inline-flex items-center justify-center px-2 py-1 mr-2 text-sm font-semibold leading-none bg-white hover:bg-gray-100 text-gray-400 border border-gray-200 rounded-full">' + result['type'] + '</span>'
                if result['link'] =='':
                    r += '<p>' + badge + result['name'] + '<br>' + '</p>'
                else:
                    r += '<p>' + badge + '<a class="text-gray-900 hover:text-red-600 no-underline hover:no-underline" target="_blank" href="'+ result['link']+ '">' + result['name'] + '</a>' + '<br>' + '</p>'
        else:
            r = '<p class="text-gray-400">Adding soon</p>'
        outfile.write(header.assemble() + '<div class="space-y-1">' + r + '</div>') 
        
        # print uncategorized videos
        if video['category'] == '_placeholder': print(video['id'])