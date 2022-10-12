import matplotlib.pyplot as plt
import numpy as np
import codecs
import os
import json
from BarGraph import font, member_list

def make_plot(member):
    path = "../json/counts_json/all_media/{}_all_media_count.json".format(member)
    try:
        fp = codecs.open(path, "r", "utf-8")
        json_data = json.load(fp)

        i = 0
        x = []
        count = []
        year_months = [] #yy-mm
        
        for data in json_data:
            count.append(data["count"])
            s = "'" + str(data["year"]-2000) + "-" + str(data["month"])
            year_months.append(s)
        
        for _ in range(len(count)):
            i += 1
            x.append(i)
        
        y_max = max(count) + 2

        fig = plt.figure(figsize=(60, 40))
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(x, count, marker="o")
        plt.title("{}の出演回数推移".format(member), fontname=font, fontsize=80)
        plt.xlabel("年-月", fontname=font, fontsize=60)
        plt.ylabel("出演回数", fontname=font, fontsize=60)
        plt.xticks(x[0:], year_months, fontsize=25)
        plt.yticks(np.arange(0, y_max, 2), fontsize=30)
        plt.savefig("PlotGraphs/{}_all_media_PlotGraph.svg".format(member))

        fp.close()
    except:
        return

for member in member_list:
    make_plot(member)