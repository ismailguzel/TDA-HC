from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import gudhi as gd
import numpy as np
import pandas as pd
import disarray
import json
import sys
from scipy.spatial.distance import euclidean
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist, squareform, cdist
from sklearn.metrics import confusion_matrix
#from sklearn.metrics.cluster import pair_confusion_matrix
from math import *
from decimal import Decimal
import glob
from sklearn.metrics import homogeneity_score, v_measure_score, adjusted_rand_score
from sklearn.metrics import adjusted_mutual_info_score, fowlkes_mallows_score, completeness_score
from sklearn.metrics import mutual_info_score, adjusted_rand_score
from sklearn.metrics import silhouette_score
from scipy.stats import entropy

def maxDist(p):
    n = len(p)
    maxm = 0
    for i in range(n):
        for j in range(i + 1, n):
            maxm = max(maxm, euclidean(p[i], p[j]))
    return maxm

def All2One(filename):
    file_list = glob.glob(filename)
    Distance_Matrix_List = [np.load(file) for file in file_list ]
    Final_Distance_Matrix = Distance_Matrix_List[0]
    for x in Distance_Matrix_List:
        Final_Distance_Matrix = np.where(Final_Distance_Matrix <= x,
                                         Final_Distance_Matrix, x)
    return(Final_Distance_Matrix)

def Cluster_Method(Data, Metric , Method, Criterion,
                   t, Plot = True, Distance = True ):
    if (Distance):
        hc = linkage(squareform(Data), method = Method)
    else:
        hc = linkage(pdist(X = Data, metric = Metric), method = Method)
    if (Plot):
        dendrogram(hc);
    return(fcluster(hc, t = t , criterion = Criterion)-1) 

from scipy.optimize import linear_sum_assignment as linear_assignment

######### Kullanılan Confusion Matrix Ayari ####
def revised_cm(cm):
    maksyerler = np.argmax(cm, axis=1)
    for i,x in enumerate(maksyerler):
        cm[i,[i,x]] = cm[i,[x,i]]
    return cm
######## Minkowski ####
def p_root(value, root):  
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), 3)
  
def minkowski_distance(x, y, p_value=1/2):
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(x, y)), p_value))

from scipy.optimize import linear_sum_assignment as linear_assignment

def _make_cost_m(cm):
    s = np.max(cm)
    return (- cm + s)

def replace_cm(cm):
    indexes = linear_assignment(_make_cost_m(cm))
    cm_new = np.empty(cm.shape)
    for i,j in zip(indexes[0],indexes[1]):
        cm_new[:,i] = cm[:,j]
    return cm_new
def replace_pred(cm,y_pred):
    indexes = linear_assignment(_make_cost_m(cm))
    y_pred_new = np.empty(y_pred.shape)
    for i,j in zip(indexes[0],indexes[1]):
        y_pred_new[np.where(y_pred == j)] = i
    return y_pred_new

def Unsupervised_Scores(Methods, Metrics, pt_cloud, minkowski, hom_distance,n_cluster,y,function):
    Result = pd.DataFrame(data=None, columns = Methods, index = Metrics)
    for method in Methods:
        for metric in Metrics:
            y_pred = Cluster_Method(Data=pt_cloud, Metric = metric, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=False)
            Result.loc[metric, method] = function(y, y_pred)
        
        y_pred_mink = Cluster_Method(Data=minkowski, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        Result.loc['minkowski',method] = function(y, y_pred_mink)
        
        y_pred_hom = Cluster_Method(Data=hom_distance, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        Result.loc['homological',method] = function(y, y_pred_hom)

    Result[function.__name__] = Result.aggregate(func='max', axis = 1)
    for distance in Result.index:
        Result.loc[distance,'method']= Result.columns[np.argmax(Result.loc[distance,:])]
    Result.drop(Methods,axis=1, inplace=True)
    return(Result)

def Supervised_Scores_hungarian(Methods, Metrics, pt_cloud, minkowski, hom_distance,n_cluster,y,function):
    Result = pd.DataFrame(data=None, columns = Methods, index = Metrics)
    for method in Methods:
        for metric in Metrics:
            y_pred = Cluster_Method(Data=pt_cloud, Metric = metric, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=False)
            cm = replace_cm(confusion_matrix(y,y_pred)).astype(int)
            # cm = revised_cm(confusion_matrix(y,y_pred)).astype(int)
            # cm = confusion_matrix(y,y_pred).astype(int)
            df = pd.DataFrame(cm, index= np.arange(n_cluster), columns=np.arange(n_cluster)) 
            Result.loc[metric, method] = df.da.export_metrics().loc[function,'micro-average']

        y_pred_mink = Cluster_Method(Data=minkowski, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        cm = replace_cm(confusion_matrix(y,y_pred_mink)).astype(int)
        # cm = revised_cm(confusion_matrix(y,y_pred_mink)).astype(int)
        # cm = confusion_matrix(y,y_pred_mink).astype(int)
        df = pd.DataFrame(cm, index= np.arange(n_cluster), columns=np.arange(n_cluster)) 
        Result.loc['minkowski', method] = df.da.export_metrics().loc[function,'micro-average']

        y_pred_hom = Cluster_Method(Data=hom_distance, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        cm = replace_cm(confusion_matrix(y,y_pred_hom)).astype(int)
        # cm = revised_cm(confusion_matrix(y,y_pred_hom)).astype(int)
        # cm = confusion_matrix(y,y_pred_hom).astype(int)
        df = pd.DataFrame(cm, index= np.arange(n_cluster), columns=np.arange(n_cluster)) 
        Result.loc['homological', method] = df.da.export_metrics().loc[function,'micro-average']
    Result.fillna(value=0.00001, inplace = True)
    Result['hungarian_max_'+function] = Result.aggregate(func='max', axis = 1)
    for distance in Result.index:
        Result.loc[distance,'method']= Result.columns[np.argmax(Result.loc[distance,:])]
    Result.drop(Methods,axis=1, inplace=True)
    return Result

def Sil_Scores(Methods, Metrics, pt_cloud, minkowski, hom_distance,n_cluster, function):
    Result = pd.DataFrame(data=None, columns = Methods, index = Metrics)
    for method in Methods:
        for metric in Metrics:
            y_pred = Cluster_Method(Data=pt_cloud, Metric = metric, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=False)
            Result.loc[metric, method] = function(pt_cloud, y_pred)

        y_pred_mink = Cluster_Method(Data=minkowski, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        Result.loc['minkowski', method] = function(minkowski, y_pred, metric='precomputed')

        y_pred_hom = Cluster_Method(Data=hom_distance, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        if len(np.unique(y_pred_hom))== n_cluster:
            Result.loc['homological', method] = function(hom_distance, y_pred_hom, metric='precomputed')
        else:
            Result.loc['homological', method] = 0

    Result[function.__name__] = Result.aggregate(func='max', axis = 1)
    for distance in Result.index:
        Result.loc[distance,'method']= Result.columns[np.argmax(Result.loc[distance,:])]
    Result.drop(Methods,axis=1, inplace=True)
    return(Result)


def Entropy(Methods, Metrics, pt_cloud, minkowski, hom_distance,n_cluster):
    Result = pd.DataFrame(data=None, columns = Methods, index = Metrics)
    for method in Methods:
        for metric in Metrics:
            y_pred = Cluster_Method(Data=pt_cloud, Metric = metric, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=False)
            Result.loc[metric, method] = entropy(np.unique(y_pred, return_counts=True)[1]/pt_cloud.shape[0])

        y_pred_mink = Cluster_Method(Data=minkowski, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        Result.loc['minkowski', method] = entropy(np.unique(y_pred, return_counts=True)[1]/pt_cloud.shape[0])

        y_pred_hom = Cluster_Method(Data=hom_distance, Metric = None, Method = method, t=n_cluster, Criterion = 'maxclust', Plot=False, Distance=True)
        Result.loc['homological', method] = entropy(np.unique(y_pred, return_counts=True)[1]/pt_cloud.shape[0])
    #Result['entropy'] = Result.aggregate(func='max', axis = 1)
    #for distance in Result.index:
    #    Result.loc[distance,'method']= Result.columns[np.argmax(Result.loc[distance,:])]
    #Result.drop(Methods,axis=1, inplace=True)
    return(Result)



def sil_score_plot(Methods, Metrics, pt_cloud, minkowski, hom_distance, n_cluster_list, function):
    plt.figure(figsize = (10,6) )
    for i in n_cluster_list:
        Unsup_Silhoutte = Sil_Scores(Methods, Metrics, pt_cloud, minkowski, hom_distance, i, function)
        plt.plot(Unsup_Silhoutte.index, Unsup_Silhoutte.silhouette_score, 'o-', label = 'n_cluster_'+str(i))


    plt.xticks(rotation = 45 )
    plt.vlines(x=5, ymin = 0, ymax = Unsup_Silhoutte.silhouette_score.max(), linestyles='dashed', colors = 'red')
    plt.legend();
    
def sil_score_plot_1(Methods, Metrics, pt_cloud, minkowski, hom_distance, n_cluster_list, function, title):

    temp = []
    for i in n_cluster_list:
        temp.append(Sil_Scores(Methods, Metrics, pt_cloud, minkowski, hom_distance, i, function).T)
    sil_n_cluster = pd.concat(temp, axis=0)
    sil_n_cluster.drop(['method'], axis = 0,inplace=True)
    sil_n_cluster.index = n_cluster_list
    plt.figure(figsize = (10,6) )
    for i in sil_n_cluster.columns:
        plt.plot(sil_n_cluster.index, sil_n_cluster[i], 'o-', label = i)
    # plt.vlines(x=5, ymin = 0, ymax = Unsup_Silhoutte.silhouette_score.max(), linestyles='dashed', colors = 'red')
    plt.legend()
    plt.xticks(n_cluster_list, fontsize = 20)
    plt.yticks(fontsize = 20)
    #plt.title(title, fontsize = 18)
    plt.xlabel('Number of Clusters', fontsize = 22)
    plt.savefig("Scores/"+title + "/"+title +"_silhouette.png", dpi = 240)
    
    
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, KFold, cross_val_score

def mykernel(distance):
    return np.exp(-(distance**2)/(2*distance.var()))

def KNN_SVC(Dist_Metrics, y, k = 5, cv = 5, Scoring = 'accuracy'):
    Result_knn = pd.DataFrame(data=None, columns = ['knn_'+Scoring], index = Dist_Metrics.keys())
    Result_svc = pd.DataFrame(data=None, columns = ['svc_'+Scoring], index = Dist_Metrics.keys())
    for metric in Dist_Metrics.keys():
        model_knn = KNeighborsClassifier(n_neighbors = k, metric = "precomputed")
        cv_scores = cross_val_score(estimator= model_knn, X=Dist_Metrics[metric], y = y, cv=cv, scoring=Scoring)
        Result_knn.loc[metric, 'knn_'+Scoring] = str(np.round(cv_scores.mean(),2)) +'$\pm$' +  str(np.round(cv_scores.std(),3)) 
    for metric in Dist_Metrics.keys():
        model_svc = SVC(kernel = "precomputed", probability=True, random_state=42)
        cv_scores = cross_val_score(estimator= model_svc, X=mykernel(Dist_Metrics[metric]), y = y, cv=cv, scoring=Scoring)
        Result_svc.loc[metric, 'svc_'+Scoring] = str(np.round(cv_scores.mean(),2)) +'$\pm$' +  str(np.round(cv_scores.std(),3)) 
    return pd.concat([Result_knn, Result_svc], axis = 1)