from datetime import datetime as dt
from get_event import get_schedules
from change_json import count as cnt
import os

member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

start = dt(2019, 3, 1)
now = dt.now()
month_sub = abs(start.year - now.year)*12 + abs(start.month - now.month)

schedules = get_schedules(month_sub, 2019, 3)

for member in member_list:
    year = 2019
    month = 3
    counts = []
    for schedule in schedules:
        c = 0
        for event in schedule:
            if member in event["member"]:
                c += 1
        counts.append(c)
    for count in counts:
        cnt.count_write_json_file(member, "all_media", count, year, month)
        month += 1
        if month > 12:
            month = 1
            year += 1

