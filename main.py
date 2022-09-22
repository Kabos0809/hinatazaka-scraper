import get_event
import search_data
import change_json

while 1:
    mode = int(input("モード選択(1: メンバーごとのスケジュールjson出力, 2: メディア出演回数json出力, 6:終了): "))

    if mode == 1:
        member = input("検索するメンバー: ")
        searched_events = get_event.get_events_member(member)
        change_json.member_event_write_json_file(member, searched_events)

    if mode == 6:
        exit(1)