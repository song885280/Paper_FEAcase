# -*- coding: utf-8 -*-

"""
@File    : plot_w2v.py
@Author  : Hangcheng
@Email   : megamhc@gmail.com
@Time    : 2021/4/7 13:56
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

def draw(clo_name):
    plt.rc('font', family='Times New Roman')
    fig = plt.gca()
    dataframe = pd.read_csv("ALL_W2V.csv")
    data = np.array(dataframe[clo_name].tolist())
    # 生成数据，以10000组均值为0，方差为1的高斯分布数据为例
    n, bins, patches = plt.hist(data, 25)
    fig.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))  # 将y轴转换为百分比
    plt.xlim(0.35, 0.75)
    plt.ylabel('Quantity of case pair', fontsize=13)
    plt.xlabel('Similarity', fontsize=13)
    plt.savefig(clo_name + ".svg")


# draw("sim_w2v")
# draw("sim_original")
# draw("sim_vsm")
draw("sim_Human")