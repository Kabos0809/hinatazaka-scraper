#search from scraped data

def search_by_member(member, event_list):
    searched_event = []
    for event in event_list:
        if event['member'] in member:
            searched_event.append(event)

    return searched_event

def search_by_date(date, event_list):
    searched_event = []
    for event in event_list:
        if event['date'] == date:
            searched_event.append(event)

def search_by_category(category, event_list):
    serached_event = []
    for event in event_list:
        if event['category'] == category:
            serached_event.append(event)

def count_appearance(member, platform, event_list):
    count = 0
    if platform == "1":
        for event in event_list:
            if event['category'] == "テレビ" and event["member"] in member:
                count += 1
        return count
    elif platform == "2":
        for event in event_list:
            if event['category'] == "ラジオ" and event["member"] in member:
                count += 1
        return count
    elif platform == "3":
        for event in event_list:
            if event['category'] == "雑誌" and event["member"] in member:
                count += 1
        return count
    elif platform == "4":
        for event in event_list:
            if event['category'] == "テレビ" or event["category"] == "ラジオ" or event["category"] == "雑誌" and event["member"] in member:
                count += 1
        return count