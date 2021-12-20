# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 01:42:27 2021

@author: YJ
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('KmeansClusteringResult.csv')

#클러스트별 현재(평일/주말) 여가활동 
plt.hist(data['CLwkd1'], alpha=0.5)
plt.hist(data['CLwke1'], alpha=0.5)

#클러스터별 희망(평일/주말) 여가활동
plt.hist(data['HLwkd1'], alpha=0.5)
plt.hist(data['HLwke1'], alpha=0.5)

cluster_wkd = data['CLwkd1'].groupby(data['cluster'])
cluster_wkd.hist(alpha=0.5)

cluster1 = cluster_wkd.get_group(0)
cluster2 = cluster_wkd.get_group(1)
cluster3 = cluster_wkd.get_group(2)
cluster4 = cluster_wkd.get_group(3)
cluster5 = cluster_wkd.get_group(4)
cluster6 = cluster_wkd.get_group(5)
cluster7 = cluster_wkd.get_group(6)

f, axes = plt.subplots(3, 3, figsize=(15, 15), sharex=True)

sns.histplot(cluster1, color='b', ax=axes[0, 0])
sns.histplot(cluster2, color='g', ax=axes[0, 1])
sns.histplot(cluster3, color='r', ax=axes[0, 2])
sns.histplot(cluster4, color='c', ax=axes[1, 0])
sns.histplot(cluster5, color='m', ax=axes[1, 1])
sns.histplot(cluster6, color='y', ax=axes[1, 2])
sns.histplot(cluster7, color='lightgreen', ax=axes[2, 0])

axes[0,0].set_title("Cluster 0")
axes[0,1].set_title("Cluster 1")
axes[0,2].set_title("Cluster 2")
axes[1,0].set_title("Cluster 3")
axes[1,1].set_title("Cluster 4")
axes[1,2].set_title("Cluster 5")
axes[2,0].set_title("Cluster 6")

plt.show()

cluster_wke = data['CLwke1'].groupby(data['cluster'])
cluster_wke.hist(alpha=0.5)

cluster1 = cluster_wke.get_group(0)
cluster2 = cluster_wke.get_group(1)
cluster3 = cluster_wke.get_group(2)
cluster4 = cluster_wke.get_group(3)
cluster5 = cluster_wke.get_group(4)
cluster6 = cluster_wke.get_group(5)
cluster7 = cluster_wke.get_group(6)

f, axes = plt.subplots(3, 3, figsize=(15, 15), sharex=True)

sns.histplot(cluster1, color='b', ax=axes[0, 0])
sns.histplot(cluster2, color='g', ax=axes[0, 1])
sns.histplot(cluster3, color='r', ax=axes[0, 2])
sns.histplot(cluster4, color='c', ax=axes[1, 0])
sns.histplot(cluster5, color='m', ax=axes[1, 1])
sns.histplot(cluster6, color='y', ax=axes[1, 2])
sns.histplot(cluster7, color='lightgreen', ax=axes[2, 0])

axes[0,0].set_title("Cluster 0")
axes[0,1].set_title("Cluster 1")
axes[0,2].set_title("Cluster 2")
axes[1,0].set_title("Cluster 3")
axes[1,1].set_title("Cluster 4")
axes[1,2].set_title("Cluster 5")
axes[2,0].set_title("Cluster 6")

plt.show()