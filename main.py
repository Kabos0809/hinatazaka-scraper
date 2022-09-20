from symbol import term
import get_event
import search_data
import change_json

while 1:
    mode = int(input("モード選択(1: メンバーで探す, 2: 日にちで探す, 3: カテゴリーで探す, 4: メンバーの出演、掲載回数を数える, 5: メディア出演回数json出力, 6: メンバーごとのスケジュールjson出力, 7:終了): "))
    if mode == 1:
        event_list = get_event.get_events_any_months(int(input("検索する期間(今日からnヶ月後まで): ")))
        member = input("探すメンバー: ")
        searched_events = search_data.search_by_member(member, event_list)
        
    if mode == 6:
        member = input("検索するメンバー: ")
        searched_events = get_event.get_events_member(member)
        change_json.member_event_write_json_file(member, searched_events)

    if mode == 7:
        exit(1)