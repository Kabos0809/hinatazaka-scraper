from unicodedata import category
import requests
import time
from bs4 import BeautifulSoup


def remove_blank(text):
    text = text.replace("\n", "")
    text = text.replace("[\u3000 \t]", "")

    return text

def search_event(year, month):
    url = (
        f"https://www.hinatazaka46.com/s/official/media/list?ima=0000&dy={year}{month}"
    )
    result = requests.get(url)
    soup = BeautifulSoup(result.content, features="lxml")
    events = soup.find_all("div", {"class": "p-schedule__list-group"})
    time.sleep(3)

    return events

def search_event_info(events):
    event_date = remove_blank(events.contents[1].text)[
        :-1
    ]
    event_name = events.find_all("p", {"class":"c-schedule__text"})
    event_time = events.find_all("div", {"class":"c-schedule__time--list"})
    event_category = events.find_all("div", {"class":"p-schedule__head"})
    event_detail_link = events.find_all("li", {"class":"p-schedule__item"})
    return event_date, event_time, event_name, event_category, event_detail_link

def search_detail_info(event_time, event_name, event_category, event_detail_link):
    if not event_time == "":
        event_time_text = remove_blank(event_time.text)
    event_name_text = remove_blank(event_name.text)
    event_category_text = remove_blank(event_category.contents[1].text)
    event_link = event_detail_link.find("a").get("href")
    event_member = search_member(event_link)

    return event_time_text, event_name_text, event_category_text, event_member

def search_member(link):
    try:
        url = f"https://www.hinatazaka46.com{link}"
        result = requests.get(url)
        soup = BeautifulSoup(result.content, features="lxml")
        member = soup.find("div", {"class":"c-article__tag"}).text.replace("メンバー", "")

        time.sleep(3)
    except:
        member = ""

    return member


