from datetime import datetime
import scrape
import time

member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

#出演メンバーのリストを取得します
def get_member_list(event_member_text, member_list):
    got_member_list = []
    for member in member_list:
        if member in event_member_text:
            got_member_list.append(member)
    return got_member_list

#指定された期間のスケジュールをすべて取得します
def get_events_any_months(term_of_months):
    start_time = time.perf_counter()
    event_list = []
    now_year = datetime.now().year
    now_month = datetime.now().month
    for _ in range(term_of_months):
        month = "{:0=2}".format(
            int(now_month)
        )
        events_each_date = scrape.search_event(now_year, month)
        for event_each_date in events_each_date:
            (
                event_date_text,
                events_time,
                events_name,
                events_category,
                events_link,
            ) = scrape.search_event_info(event_each_date)

            for (event_time, event_name, event_category, event_link) in zip(events_time, events_name, events_category, events_link):
                (
                    event_time_text,
                    event_name_text,
                    event_category_text,
                    event_member_text
                ) = scrape.search_detail_info(event_time, event_name, event_category, event_link)
                members = get_member_list(event_member_text, member_list)
                event = {
                    'year': now_year,
                    'month': now_month,
                    'date': int(event_date_text),
                    'time': event_time_text,
                    'name': event_name_text,
                    'category': event_category_text,
                    'member': members,
                }

                event_list.append(event)
        now_month += 1
        if now_month > 12:
            now_year += 1
            now_month = 1
    end_time = time.perf_counter()
    t = end_time - start_time   
    print("completed!!({:.2f}s)".format(t))
    return event_list

#指定されたメンバーの１か月間のスケジュールを取得します
def get_events_member(member):
    start_time = time.perf_counter()
    event_list = []
    now_year = datetime.now().year
    now_month = datetime.now().month
    month = "{:0=2}".format(
        int(now_month)
    )
    events_each_date = scrape.search_event(now_year, month)
    for event_each_date in events_each_date:
        (
            event_date_text,
            events_time,
            events_name,
            events_category,
            events_link,
        ) = scrape.search_event_info(event_each_date)
        for (event_time, event_name, event_category, event_link) in zip(events_time, events_name, events_category, events_link):
            (
                event_time_text,
                event_name_text,
                event_category_text,
                event_member_text
            ) = scrape.search_detail_info(event_time, event_name, event_category, event_link)
            members = get_member_list(event_member_text, member_list)
            if member in members and event_category_text != "誕生日":
                event = {
                    'year': now_year,
                    'month': now_month,
                    'date': int(event_date_text),
                    'time': event_time_text,
                    'name': event_name_text,
                    'category': event_category_text,
                    'member': members,
                }
                event_list.append(event)
    
    end_time = time.perf_counter()
    t = end_time - start_time
    print("completed!!({:.2f}s)".format(t))
    
    return event_list

#指定されたカテゴリーでメンバーの出演回数を数えます
def get_member_count(member, platform, _year, _month):
    start_time = time.perf_counter()

    count = 0

    month = "{:0=2}".format(
        int(_month)
    )
    events_each_date = scrape.search_event(_year, month)
    for event_each_date in events_each_date:
        (
            _,
            events_time,
            events_name,
            events_category,
            events_link,
        ) = scrape.search_event_info(event_each_date)
        for (event_time, event_name, event_category, event_link) in zip(events_time, events_name, events_category, events_link):
            (
                _,
                _,
                event_category_text,
                event_member_text
            ) = scrape.search_detail_info(event_time, event_name, event_category, event_link)
            members = get_member_list(event_member_text, member_list)
            if member in members and event_category_text != "誕生日":
                if platform == event_category_text:
                    count += 1
                elif platform == "all_media":
                    count += 1
    end_time = time.perf_counter()
    t = end_time - start_time
    print("completed!!({:.2f}s)".format(t))
    return count

#指定された期間、指定されたメンバーのカテゴリごとの出演回数を数えます
def get_count_any_months(term_of_months, start_year, start_month, member, platform):
    start_time = time.perf_counter()
    counts = []
    now_year = start_year
    now_month = start_month
    for _ in range(term_of_months):
        count = 0
        month = "{:0=2}".format(
        int(now_month)
        )
        events_each_date = scrape.search_event(now_year, month)
        for event_each_date in events_each_date:
            (
                _,
                events_time,
                events_name,
                events_category,
                events_link
            ) = scrape.search_event_info(event_each_date)
            for (event_time, event_name, event_category, event_link) in zip(events_time, events_name, events_category, events_link):
                (
                    _,
                    _,
                    event_category_text,
                    event_member_text
                ) = scrape.search_detail_info(event_time, event_name, event_category, event_link)
                members = get_member_list(event_member_text, member_list)
                if member in members and event_category_text != "誕生日":
                    if platform == event_category_text:
                        count += 1
                    elif platform == "all_media":
                        count += 1
        counts.append(count)

        now_month += 1
        if now_month > 12:
            now_month = 1
            now_year += 1

    end_time = time.perf_counter()
    t = end_time - start_time
    print("completed!!({:.2f}s)".format(t))
    return counts

def get_schedules(term_of_months, year, start_month):
    start_time = time.perf_counter()
    event_list = []
    month = "{:0=2}".format(
        int(start_month)
    )
    for _ in range(term_of_months):
        month = "{:0=2}".format(
            int(start_month)
        )
        events = []
        events_each_date = scrape.search_event(year, month)
        for event_each_date in events_each_date:
            (
                event_date_text,
                events_time,
                events_name,
                events_category,
                events_link,
            ) = scrape.search_event_info(event_each_date)
            for (event_time, event_name, event_category, event_link) in zip(events_time, events_name, events_category, events_link):
                (
                    event_time_text,
                    event_name_text,
                    event_category_text,
                    event_member_text
                ) = scrape.search_detail_info(event_time, event_name, event_category, event_link)
                members = get_member_list(event_member_text, member_list)
                if event_category_text != "誕生日":
                    event = {
                        'year': year,
                        'month': month,
                        'date': int(event_date_text),
                        'time': event_time_text,
                        'name': event_name_text,
                        'category': event_category_text,
                        'member': members,
                    }
                    events.append(event)
       
        event_list.append(events)
        
        start_month += 1
        if start_month > 12:
            start_month = 1
            year += 1
    
    end_time = time.perf_counter()
    t = end_time - start_time
    print("completed!! {:.2f}s".format(t))

    return event_list