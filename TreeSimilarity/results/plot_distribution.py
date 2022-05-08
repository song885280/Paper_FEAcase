
'''
时间：20220507
內容：查看数据分布图
'''

import pandas as pd
import numpy as np
import csv
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker

# sim_w2v	sim_original	sim_vsm	sim_BERT	sim_Human

file_path = r'0505FEAcaseSet_cn_W2V_repair.csv'

data_frame_csv = pd.read_csv(file_path, \
                 names = ["sim_Human"], header=1, usecols = [7])
# data_df01 = data_frame_csv[['sim_original']]
# print(type(data_df01))

data_df01 = data_frame_csv['sim_Human']
print(type(data_df01))
res = data_df01.tolist()
# print(res)
print('列表长度为：'+ str(res.__len__() + 1))

# 绘图
np.random.seed(0)
plt.figure(dpi=120)
sns.set(style='dark')
sns.set_style("dark", {"axes.facecolor": "#e9f3ea"})#修改背景色
chart1 = sns.distplot(res, hist=True, kde=False, color="#098154")
# chart2 = sns.kdeplot(res, shade=True, bw=0.5, color="#098154")
plt.title('sim_Human',fontsize=15)
plt.show()