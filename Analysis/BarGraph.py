import matplotlib.pyplot as plt
import numpy as np
import json
import codecs

font = "MS Gothic"

def make_histogram(member):
    path = "../json/counts_json/all_media/{}_all_media_count.json".format(member)
    fp = codecs.open(path, "r", "utf-8")
    data = json.load(fp)
    
    index = 0
    left = []
    count = []
    year_months = [] #yyyy-mm

    for d in data:
        s = "'" + str(d["year"]-2000) + "-" + str(d["month"])
        year_months.append(s)
        count.append(d["count"])
    
    for _ in range(len(count)):
        index += 1
        left.append(index)

    y_max = int(max(count)) + 2
    fig = plt.figure(figsize=(len(count), y_max))
    ax = fig.add_subplot(111)
    ax.bar(left, count, width=0.8)
    plt.title("{}の出演回数推移".format(member), fontname=font)
    plt.xlabel("年-月", fontname=font)
    plt.ylabel("出演回数", fontname=font)
    plt.xticks(left[0:], year_months)
    plt.yticks(np.arange(0, y_max, 2))
    plt.show()

make_histogram("東村芽依")
