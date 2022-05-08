# -*- coding: utf-8 -*-

"""
@File    : plot.py
@Author  : Hangcheng
@Email   : megamhc@gmail.com
@Time    : 2021/4/6 20:57
"""

import pandas as pd
import numpy as np
import csv
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker


plt.rc('font', family='Times New Roman')


def Delta(Sim_1, Sim_2):
    return abs((Sim_1 - Sim_2) / Sim_2)


class Result:

    def __init__(self, filename):
        """

        :param filename: 结果文件名
        """
        self.Data = pd.read_csv(filename, encoding="gbk")
        self.length = self.Data.shape[0] - 1
        self.PSO_Delta = 0
        self.VSM_Delta = 0
        self.PSO_Theta = 0
        self.VSM_Theta = 0
        self.Original_Delta = 0
        self.Original_Theta = 0

    def AvrDelta(self, Mod):
        """
        计算整体的平均误差
        :param Mod:
        :return: 平均误差
        """
        index = "sim_" + Mod
        AllDelta = 0
        for i in range(0, self.length):
            Sim_1 = self.Data.loc[i][index]
            Sim_2 = self.Data.loc[i]["sim_Human"]
            AllDelta += Delta(Sim_1, Sim_2)
        return AllDelta / self.length

    def GetTheta(self, avrDelta, Mod):
        """
        计算方差
        :param avrDelta: 平均误差
        :param Mod: 算法名PSO、VSM、Original
        :return: 方差
        """
        index = "sim_" + Mod
        AllTheta = 0
        for i in range(0, self.length):
            Sim_1 = self.Data.loc[i][index]
            Sim_2 = self.Data.loc[i]["sim_Human"]
            AllTheta += pow(Delta(Sim_1, Sim_2) - avrDelta, 2)
        return AllTheta / self.length


PSO = Result("ALL_PSO.csv")

PSO.PSO_Delta = PSO.AvrDelta("PSO")
PSO.PSO_Theta = PSO.GetTheta(PSO.PSO_Delta, "PSO")
PSO.VSM_Delta = PSO.AvrDelta("VSM")
PSO.VSM_Theta = PSO.GetTheta(PSO.VSM_Delta, "VSM")
PSO.Original_Delta = PSO.AvrDelta("Original")
PSO.Original_Theta = PSO.GetTheta(PSO.Original_Delta, "Original")

print(PSO.PSO_Delta, PSO.PSO_Theta)
print(PSO.VSM_Delta, PSO.VSM_Theta)
print(PSO.Original_Delta, PSO.Original_Theta)

fig= plt.gca()
Mods = ["PSO+MultiTree", "MultiTree", "VSM"]
Delta = [PSO.PSO_Delta, PSO.Original_Delta, PSO.VSM_Delta]
Theta = [PSO.PSO_Theta, PSO.Original_Theta, PSO.VSM_Theta]
plt.bar(Mods, Delta, yerr=Theta, width=0.45, error_kw={'ecolor': '0.2', 'capsize': 5, "capthick": 1}, alpha=0.7)
plt.xticks(fontsize=13)  # 更改字体大小
plt.yticks(fontsize=13)
fig.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))  # 将y轴转换为百分比

fig.spines["top"].set_visible(False)
fig.spines["right"].set_visible(False)
plt.ylabel('Average error',fontsize=13)
# plt.title('Error compared with human judgement',fontsize=15)
plt.savefig("img/Error_analysis_pso.png")
plt.show()
