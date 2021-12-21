# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 01:13:51 2021

@author: YJ
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score, silhouette_samples
from matplotlib import cm

#data load
data= pd.read_excel('survey.xlsx')

#function to determine K of k-means 
def elbow(X) : 
   sse=[]
   for i in range(2,70) : 
      km = KMeans(n_clusters=i)
      km.fit(X)
      sse.append(km.inertia_)
   
   plt.plot(range(2,70),sse, marker='o')
   plt.title('Elbow graph')
   plt.xlabel('The number of cluster')
   plt.ylabel('SSE')
   plt.show()
   
def plotSilhouette(X, y_km) :
   cluster_labels = np.unique(y_km)
   n_clusters = cluster_labels.shape[0]
   silhouette_vals = silhouette_samples(X,y_km , metric='euclidean')
   y_ax_lower, y_ax_upper = 0,0
   yticks =[]
   
   for i, c in enumerate(cluster_labels) :
      c_silhouette_vals = silhouette_vals[y_km==c]
      c_silhouette_vals.sort()
      y_ax_upper += len(c_silhouette_vals)
      color =cm.jet(i/n_clusters)
      
      plt.barh(range(y_ax_lower,y_ax_upper),c_silhouette_vals, height=1.0, color = color)
      yticks.append((y_ax_lower+y_ax_upper)/2)
      y_ax_lower += len(c_silhouette_vals)
      
   silhoutte_avg = np.mean(silhouette_vals)
   plt.axvline(silhoutte_avg, c='r', linestyle='--')
   plt.yticks(yticks, cluster_labels)
   plt.ylabel('Cluster')
   plt.xlabel('The silhoutte coefficient values')
   plt.show()
   
   
def scoreSilhouette(X) : 
   silscore=[]
   for i in range(2,11) : 
      kmean = KMeans(n_clusters=i)
      kmean.fit(X)
      kmean_label = kmean.labels_
      score = silhouette_score(X, kmean_label)
      silscore.append(score)
      
   plt.plot(range(2,11),silscore)
   plt.xlabel('The number of cluster')
   plt.ylabel('Silhouette score')
   plt.title('Sihouette score, Range 2 to 11')
   plt.show()
   
   
if __name__ == '__main__' :
   new_data = data.iloc[:,[2,3,4,9,10]]

   data_norm = (new_data - np.mean(new_data))/np.std(new_data)

   #rule of thrumb k = np.sqrt(len(data)/2) , normal method to determine k
   k74 = KMeans(n_clusters=74)
   k74.fit(data_norm)
   k74_label = k74.labels_
   silhouette_score(data_norm,k74_label)
   
   #check intertia == SSE 
   elbow(data_norm)
   #AND silhouette score in 2<k<11
   scoreSilhouette(data_norm)
   
   # k=7 or k=8
   # k = 7
   k7 = KMeans(n_clusters=7)
   k7.fit(data_norm)
   k7_label = k7.labels_
   y_km = k7.predict(data_norm)
   silhouette_score(data_norm, k7_label)   
   plotSilhouette(data_norm, y_km)
   
   # k = 8
   k8 = KMeans(n_clusters=8)
   k8.fit(data_norm)
   k8_label = k8.labels_
   y_km = k8.predict(data_norm)
   silhouette_score(data_norm, k8_label)   
   plotSilhouette(data_norm, y_km)
   
   # determine k = 7 and make column cluster by each row 
   data_norm['cluster7'] = k7_label
   
   data['cluster'] = data_norm['cluster7']
   data.to_csv('KmeansClusteringResult.csv', encoding='utf-8-sig', index=None) 
   
