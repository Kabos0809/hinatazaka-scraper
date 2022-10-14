from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import codecs
import json
from BarGraph import font, member_list

plt.rcParams["font.family"] = font

def make_plot():
    for member in member_list:
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

            fig = plt.figure(figsize=(60, 40))
            ax = fig.add_subplot(1, 1, 1)
            ax.plot(x, count, marker="o", markersize=20, lw=4)
            plt.title("{}の出演回数推移".format(member), fontname=font, fontsize=80)
            plt.xlabel("年-月", fontname=font, fontsize=60)
            plt.ylabel("出演回数", fontname=font, fontsize=60)
            plt.xticks(x[0:], year_months, fontsize=25)
            plt.yticks(np.arange(0, 40, 2), fontsize=30)
            plt.savefig("PlotGraphs/svg/{}_all_media_PlotGraph.svg".format(member))
            plt.savefig("PlotGraphs/png/{}_all_media_PlotGraph.png".format(member))
            fp.close()
        except:
            continue

def make_any_plots():
    n = int(input("人数: "))
    i = 1
    x = []
    members = []
    year_months = []
    counts = {}
    for _ in range(n):
        members.append(input("{}人目: ".format(i)))    
        i += 1
    for member in members:
        count = []
        p = 0
        path = "../json/counts_json/all_media/{}_all_media_count.json".format(member)
        try:
            fp = codecs.open(path, "r", "utf-8")
            json_data = json.load(fp)
            fp.close()
            for data in json_data:
                count.append(data["count"])
                if len(x) == 0:
                    s = "'" + str(data["year"]-2000) + "-" + str(data["month"])
                    year_months.append(s)  
            if len(x) == 0:
                for _ in range(len(count)):
                    p += 1
                    x.append(p)
            counts[member] = count
        except:
            print("err")
            continue
    fig = plt.figure(figsize=(60, 40))
    ax = fig.add_subplot(1, 1, 1)
    m = ""
    for member in members:
        m += member + "-"
        ax.plot(x, counts[member], label=member, marker="o", markersize=20, lw=4)
    ax.set_title("{}の出演回数推移".format(m), fontname=font, fontsize=80)
    ax.set_xlabel("年-月", fontname=font, fontsize=60)
    ax.set_ylabel("出演回数", fontname=font, fontsize=60)
    ax.legend(fontsize=45)
    plt.xticks(x[0:], year_months, fontsize=25)
    plt.yticks(np.arange(0, 40, 2), fontsize=30)
    plt.savefig("Any_plots/svg/{}_members_plot.svg".format(m))
    plt.savefig("Any_plots/png/{}_members_plot.png".format(m))
    plt.close()
    
make_any_plots()

    