import matplotlib.pyplot as plt
import numpy as np
import json
import codecs

font = "MS Gothic"
member_list = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花", "東村芽依", 
                "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌", "上村ひなの",
                    "髙橋未来虹", "森本茉莉", "山口陽世"]

def make_bargraph(member):
    path = "../json/counts_json/all_media/{}_all_media_count.json".format(member)
    
    try:
        fp = codecs.open(path, "r", "utf-8")

        data = json.load(fp)

        index = 0
        x = []
        count = []
        year_months = [] #yy-mm

        for d in data:
            s = "'" + str(d["year"]-2000) + "-" + str(d["month"])
            year_months.append(s)
            count.append(d["count"])

        for _ in range(len(count)):
            index += 1
            x.append(index)

        fig = plt.figure(figsize=(60, 40), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(x, count, width=0.8)
        plt.title("{}の月別出演回数".format(member), fontname=font, fontsize=80)
        plt.xlabel("年-月", fontname=font, fontsize=60)
        plt.ylabel("出演回数", fontname=font, fontsize=60)
        plt.xticks(x[0:], year_months, fontsize=25)
        plt.yticks(np.arange(0, 40, 2), fontsize=30)
        plt.savefig("BarGraphs/svg/{}_all_media_BarGraph.svg".format(member))
        plt.savefig("BarGraphs/png/{}_all_media_BarGraph.png".format(member))

        fp.close()
    except:
        return
    finally:
        plt.close()
    return

for member in member_list:
    make_bargraph(member)
