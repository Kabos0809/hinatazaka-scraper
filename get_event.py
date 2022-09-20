from datetime import datetime
import scrape

def get_events_any_months(term_of_months):
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

                event = {
                    'year': now_year,
                    'month': now_month,
                    'date': event_date_text,
                    'time': event_time_text,
                    'name': event_name_text,
                    'category': event_category_text,
                    'member': event_member_text,
                }

                event_list.append(event)
        now_month += 1
        if now_month > 12:
            now_year += 1
            now_month = 1
    print("completed!!")
    return event_list

def get_events_member(member):
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
            if member in event_member_text:
                event = {
                    'year': now_year,
                    'month': now_month,
                    'date': event_date_text,
                    'time': event_time_text,
                    'name': event_name_text,
                    'category': event_category_text,
                    'member': event_member_text,
                }
                event_list.append(event)
    print("completed!!")
    return event_list