import binary_search
import search_data
import json
import codecs
import os
from datetime import datetime

def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))

month = datetime.now().month
date = datetime.now().date
member_count = {"更新日":str(month)+str(date)+"時点", "潮紗理菜":0, "影山優佳":0, "加藤史帆":0, "齋藤京子":0, "佐々木久美":0, "佐々木美玲":0, "高瀬愛奈":0, "高本彩花":0, "東村芽依":0, "金村美玖":0, "河田陽菜":0, "小坂菜緒":0, "富田鈴花":0, "丹生明里":0, "濱岸ひより":0, "松田好花":0, "宮田愛萌":0, "渡邉美穂":0, "上村ひなの":0, "髙橋未来虹":0, "森本茉莉":0, "山口陽世":0}

def event_write_json_file(events):
    today = datetime.now()
    path = './json/{}_{}_events.json'.format(today.year, today.month)
    try:
        if not os.path.isfile(path):
            json_file = codecs.open(path, 'w', 'utf-8')
            json.dump(events, json_file, default=json_serial, ensure_ascii=False)

            return
        else:
            json_file = codecs.open(path, mode='r')
            json_data = json.loads(json_file)

            for data in json_data:
                for event in events:
                    if event['year'] == data['year'] and event['month'] == data['month'] and event['date'] == data['date'] and event['name'] == data['name']:
                        continue
                    else:
                        i = binary_search.binary_search(json_data, event)
                        json_data.insert(i, event)
            json_file = codecs.open(path, 'w', 'utf-8')
            json.dump(json_data, json_file, default=json_serial, ensure_ascii=False)
            
            return
    finally:
        json_file.close()
    

def count_media_write_json_file(events):
    today = datetime.now()
    path = './json/counts_json/{}_{}_counts.json'.format(today.year, today.month)
    try:
        if not os.path.isfile(path):
            json_file = codecs.open(path, 'w', 'utf-8')
            for key in member_count.keys():
                member_count[key] += search_data.count_appearance(key, 4, events)
            json.dump(member_count, json_file, default=json_serial, ensure_ascii=False, indent=3)

            return
        else:
            json_file = codecs.open(path, mode='r')
            json_data = json.load(json_file)
            for key in member_count.keys():
                member_count[key] += search_data.count_appearance(key, 4, events)
            save_data = [json_data, member_count]
            json_file = codecs.open(path, 'w', 'utf-8')
            json.dump(save_data, json_file, default=json_serial, ensure_ascii=False, indent=3)

            return
    finally:
        json_file.close()

def member_event_write_json_file(member, events):
    today = datetime.now()
    path = './json/member/{}_{}_{}_events.json'.format(member, today.year, today.month)
    json_file = codecs.open(path, 'w', 'utf-8')
    json.dump(events, json_file, default=json_serial, ensure_ascii=False, indent=3)

    json_file.close()

    return