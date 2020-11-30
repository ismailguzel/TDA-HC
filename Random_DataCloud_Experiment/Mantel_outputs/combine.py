# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:15:01 2020

@author: ismailguzel
"""


import pandas as pd
import numpy as np

df1 = pd.read_csv("test_significance.csv")
df2 = pd.read_csv("test_statistic.csv")

DF = pd.concat([df1.iloc[:,1], df2.iloc[:,1]], axis=1)
DF.columns = ["Significance", "Mantel_Statistic"]
DF.to_csv("randomly100_results.csv")


DF.mean(axis=0)

np.round(DF.mean(axis=0),3)



print("MAximum:\n",DF.max(axis=0))
print("\n Median: \n",DF.median(axis=0))
print("\n Mean: \n",DF.mean(axis=0))



plt.boxplot(DF.Mantel_Statistic)


DF.Mantel_Statistic.hist()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.hist(DF.Mantel_Statistic, bins=15, facecolor='green', width=0.004)
#ax.set_xticks(np.arange(0.70,1.0001,0.05))
plt.savefig("results_mantel.png", dpi=300)




fig, ax = plt.subplots(1,2)
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
ax[1].hist(DF.Mantel_Statistic, bins=30, facecolor='green', width=0.004)
ax[1].set_xticks(np.arange(0.70,1.0001,0.05))

ax[0].boxplot(DF.Mantel_Statistic, flierprops = dict(markerfacecolor='g', marker='D') )
# par1 = ax[1].twinx()
# par1.spines['right'].set_position(('axes',1))
# par1.set_yticks(np.arange(0.70,1.0001,0.05))
ax[0].get_yaxis().set_visible(True)
# plt.title('Histogram of Mantel Statistic')

plt.savefig("results_mantel.png", dpi=300)

















