from datetime import datetime
import get_event
import search_data
import change_json

while 1:
    mode = int(input("モード選択(1: メンバーごとのスケジュールjson出力, 2: 今月のカテゴリ別出演回数json出力, 3: 時期指定カテゴリ別出演回数json出力, 6:終了): "))
    today = datetime.now()

    if mode == 1:
        member = input("検索するメンバー: ")
        searched_events = get_event.get_events_member(member)
        change_json.member_event_write_json_file(member, searched_events)

    if mode == 2:
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

        change_json.count_write_json_file(member, platform, count, today.year, today.month)
    
    if mode == 3:
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

        change_json.count_write_json_file(member, platform, count, year, month)
        

    if mode == 6:
        exit(1)