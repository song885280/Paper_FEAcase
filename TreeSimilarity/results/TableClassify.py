
'''
将单元格中的相似性值进行分类（1-5）；
1表示最相似；5表示最不相似
五组分别为："sim_w2v", "sim_original", "sim_vsm", "sim_BERT", "sim_Human"
'''
import csv
import pandas as pd

file = "0505FEAcaseSet_en_W2V_repair.csv"
Read_TableData = pd.read_csv(file, encoding="gbk")
lst1 = []
for cellvalue in range(len(Read_TableData)):
    i = float(Read_TableData["sim_Human"][cellvalue])
    lst1.append(i)

for j in lst1:
    if j >= 0 and j < 0.4:
        print('0.2')
    if j >= 0.4 and j < 0.55:
        print('0.4')
    if j >= 0.55 and j < 0.7:
        print('0.6')
    if j >= 0.7 and j < 0.85:
        print('0.8')
    if j >= 0.85 and j<= 1:
        print('1.0')

