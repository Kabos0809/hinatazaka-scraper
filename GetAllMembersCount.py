import get_event
import change_json
import os

member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

def GetAllMemberCount():
    year = 2019
    month = 3
    term_of_month = 44
    platform = "all_media"
    schedules = get_event.get_schedules(term_of_month, year, month)

    for member in member_list:
        year = 2019
        month = 3
        counts = []
        path = "./json/counts_json/all_media/{}_all_media_count.json".format(member)
        if os.path.isfile(path):
            print("データが存在しています")
            continue
        else:
            for schedule in schedules:
                c = 0
                for event in schedule:
                    if member in event["member"]:
                        c += 1
                counts.append(c)

            for count in counts:
                change_json.count_write_json_file(member, platform, count, year, month)
                month += 1
                if month > 12:
                    month = 1
                    year += 1
    
GetAllMemberCount()