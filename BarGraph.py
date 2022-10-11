import matplotlib.pyplot as plt
import numpy as np
import json
import codecs

font = "MS Gothic"
member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

def make_histogram(member):
    path = "../json/counts_json/all_media/{}_all_media_count.json".format(member)
    
    try:
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
        plt.savefig("BarGraphs/{}_all_media_BarGraph.svg".format(member))

        fp.close()
    except:
        return
    
    return

for member in member_list:
    make_histogram(member)
