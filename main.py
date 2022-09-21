import get_event
import search_data
import change_json

while 1:
    mode = int(input("モード選択(1: メンバーで探す, 2: カテゴリーで探す, 3: メンバーのメディア露出回数を数える, 4: メディア出演回数json出力, 5: メンバーごとのスケジュールjson出力, 6:終了): "))
    if mode == 1:
        event_list = get_event.get_events_any_months(int(input("検索する期間(今月からnヶ月後まで): ")))
        member = input("探すメンバー: ")
        searched_events = search_data.search_by_member(member, event_list)
        print(searched_events)

    if mode == 2:
        event_list = get_event.get_events_any_months(int(input("検索する期間(今月からnヶ月後まで): ")))
        category = input("探すカテゴリー: ")
        searched_events = search_data.search_by_category(category, event_list)
        print(searched_events)

    if mode == 5:
        member = input("検索するメンバー: ")
        searched_events = get_event.get_events_member(member)
        change_json.member_event_write_json_file(member, searched_events)

    if mode == 6:
        exit(1)