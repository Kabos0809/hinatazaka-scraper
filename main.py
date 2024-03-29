from datetime import datetime
import get_event
import change_json

member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

while 1:
    mode = int(input("モード選択(1: 今月のカテゴリ別出演回数json出力, 2: 時期指定カテゴリ別出演回数json出力, 3: 期間指定カテゴリ別出演回数json出力, 0:終了): "))
    today = datetime.now()
    if mode == 1:
        member = input("検索するメンバー: ")
        platform = int(input("カテゴリ指定(1:テレビ, 2:ラジオ, 3: 雑誌, 4:メディアすべて): "))
        if platform == 1:
            platform = "テレビ"
        elif platform == 2:
            platform = "ラジオ"
        elif platform == 3:
            platform = "雑誌"
        elif platform == 4:
            platform = "all_media"
        count = get_event.get_member_count(member, platform, today.year, today.month)
        if platform == "テレビ":
            platform = "tv"
        elif platform == "ラジオ":
            platform = "radio"
        elif platform == "雑誌":
            platform = "magazine"
        change_json.count.count_write_json_file(member, platform, count, today.year, today.month)
    if mode == 2:
        member = input("検索するメンバー: ")
        year = int(input("指定する年(西暦): "))
        month = int(input("指定する月: "))
        platform = int(input("カテゴリ指定(1:テレビ, 2:ラジオ, 3: 雑誌, 4:メディアすべて): "))
        if platform == 1:
            platform = "テレビ"
        elif platform == 2:
            platform = "ラジオ"
        elif platform == 3:
            platform = "雑誌"
        elif platform == 4:
            platform = "all_media"
        count = get_event.get_member_count(member, platform, year, month)
        if platform == "テレビ":
            platform = "tv"
        elif platform == "ラジオ":
            platform = "radio"
        elif platform == "雑誌":
            platform = "magazine"
        change_json.count.count_write_json_file(member, platform, count, year, month)
    if mode == 3:
        member = input("検索するメンバー: ")
        year = int(input("スタートの年(西暦): "))
        month = int(input("スタートの月: "))
        term_of_month = int(input("検索する期間(nヶ月): "))
        platform = int(input("カテゴリ指定(1:テレビ, 2:ラジオ, 3: 雑誌, 4:メディアすべて): "))
        if platform == 1:
            platform = "テレビ"
        elif platform == 2:
            platform = "ラジオ"
        elif platform == 3:
            platform = "雑誌"
        elif platform == 4:
            platform = "all_media"
        counts = get_event.get_count_any_months(term_of_month, year, month, member, platform)
        if platform == "テレビ":
            platform = "tv"
        elif platform == "ラジオ":
            platform = "radio"
        elif platform == "雑誌":
            platform = "magazine"
        for count in counts:
            change_json.count.count_write_json_file(member, platform, count, year, month)
            month += 1
            if month > 12:
                month = 1
                year += 1
    if mode == 0:
        exit(1)