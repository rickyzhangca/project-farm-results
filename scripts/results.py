
import json

def add_results_field():
    washed = []
    pre = []
    with open('scripts/washed.json') as f:
        pre = json.load(f)
    for video in pre:
        video['results'] = []
        washed.append(video)
    json_object = json.dumps(washed, indent = 4, ensure_ascii=False) 
    with open("scripts/washed.json", "w") as outfile: 
        outfile.write(json_object) 

def enter_results():
    washed = []
    with open('scripts/washed.json') as f:
        washed = json.load(f)
    while True:
        date = input('enter date or e(exit): ')
        if date == 'e': break
        date = date.split('/')
        if len(date[0]) == 1: date[0] = '0' + date[0]
        if len(date[1]) == 1: date[1] = '0' + date[1]
        date = date[2] + '-' + date[0] + '-' + date[1]
        dicts = []
        for video in washed:
            if video['date'] == date:
                dicts = []
                while True:
                    new = input('another dict? y/n')
                    if new == 'n': break
                    dict = {}
                    type = input('enter type: ')
                    dict['type'] = type
                    name = input('name: ')
                    dict['name'] = name
                    # link = input('link: ')
                    # dict['link'] = link
                    dict['link'] = ''
                    dicts.append(dict)
                for dict in dicts:
                    video['results'].append(dict)
    json_object = json.dumps(washed, indent = 4, ensure_ascii=False) 
    with open("scripts/washed.json", "w") as outfile: 
        outfile.write(json_object) 

def convert_date():
    while True:
        date = input('enter date or exit: ')
        if date == 'close': break
        date = date.split('/')
        if len(date[0]) == 1: date[0] = '0' + date[0]
        if len(date[1]) == 1: date[1] = '0' + date[1]
        date = date[2] + '-' + date[0] + '-' + date[1]
        print(date)
        
enter_results()