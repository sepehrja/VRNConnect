# This is a sample Python script.

import csv
import os

import bct
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
# importing the data
from numpy import ndarray

#for standAlone running
# project_path = '../../Resources/'
# res_path = project_path

#for Unity running
project_path = os.getcwd()+'\\externalFiles\\'
res_path = os.getcwd()+'\\Assets\\Resources\\'

df_region_color = pd.read_csv(f'{project_path}HCP-MMP1_RegionColor.csv', skipfooter=19, engine='python')
df_region_list = pd.read_csv(f'{project_path}HCP-MMP1_UniqueRegionList.csv')
df_main = pd.read_csv(f'{project_path}hcpmmp1.csv', skipfooter=19, header=None, engine='python')

# converting to ndarray
ndarray_sub = np.asarray(list(df_main.get(0)))
ndarray_main = np.resize(np.asarray(dtype=float, a=ndarray_sub[0].split(' ')), (1, 360))
# converting values to float and appending to the main ndarray + removing rows 360-379
for x in range(1, ndarray_sub.size):
    # removing columns 360-379
    tmp: ndarray = np.resize(np.asarray(dtype=float, a=ndarray_sub[x].split(' ')), (1, 360))
    # print(tmp)
    ndarray_main = np.append(ndarray_main, tmp, axis=0)

# creating the binary connection graph
# ndarray_main_bin = np.logical_or(ndarray_main,ndarray_main)
ndarray_main_bin = bct.binarize(ndarray_main, True)
# ndarray_main = np.reshape(ndarray_main,(359,359))
# columns = range(0,360)
# df_main = pd.DataFrame(data=df_main, index=columns).T
print(df_main)
# print(df_main.dtypes)
print(df_region_list)
print(df_region_color)
print(ndarray_main)
print(ndarray_main_bin)

# clean_main_df = pd.DataFrame()
#
# for row in df_main.iterrows():
#      print(row.__getitem__(1).values.__getitem__(0).split(' '))

# print(clean_df)

print('Result of the algorithms:\n=========================')
# bct.assortativity_wei(CIJ=ndarray_main,flag=0)
wei_ass = bct.assortativity_wei(CIJ=ndarray_main, flag=0)
bin_ass = bct.assortativity_bin(ndarray_main_bin, flag=0)
print('Result of the assortativity_wei:' + wei_ass.__str__())
print('Result of the assortativity_bin:' + bin_ass.__str__())

# breadth_dist = bct.breadthdist(ndarray_main_bin)
bfsFileName = 'breadth_distance'
weighted_shortest_paths_FileName = 'weighted_shortest_paths'
floydFileName = 'floyd_shortest_paths'
# pd.DataFrame.from_records(breadth_dist[1]).to_json(f'{res_path}{bfsFileName}.json')
# pd.DataFrame.from_records(breadth_dist[1]).to_csv(f'{res_path}{bfsFileName}.csv')
# pd.DataFrame.from_records(breadth_dist[1]).to_csv(f'{res_path}{bfsFileName}.txt')
# print('Result of the breadth_dist:')
# print(breadth_dist[1])  # -we can get number of disconnected nodes from this one-#
# min_dist = breadth_dist[1].min()
# max_dist = breadth_dist[1].max()

clus_coef = bct.clustering_coef_wu(ndarray_main)
print('Result of the clustering coef:')
print(clus_coef)
clusCoefFileName = 'clustering_coef'
pd.DataFrame.from_dict(clus_coef).to_json(f'{res_path}{clusCoefFileName}.json')
pd.DataFrame.from_dict(clus_coef).to_csv(f'{res_path}{clusCoefFileName}.csv')
pd.DataFrame.from_dict(clus_coef).to_csv(f'{res_path}{clusCoefFileName}.txt')

# bct.betweenness_wei
# bct.agreement_weighted()
# bct.backbone_wu
# bct.betweenness_bin
# 1.bct.distance_bin()
# 2.bct.distance_wei() -> have to change strength to weight (strong node have lesser weight)
# 3.bct.retrieve_shortest_path()
##################################################################
header = ['algorithm_name', 'result', 'algorithm_cat']
data = [
    ['assortativity_wei', wei_ass, 'CORE'],
    ['assortativity_bin', bin_ass, 'CORE'],
    # ['breadth_distance_min', min_dist, 'BFS'],
    # ['breadth_distance_max', max_dist, 'BFS'],
    ['breadth_distance_matrix', f'{bfsFileName}.csv', 'BFS'],
    ['weighted_distance_matrix', f'{weighted_shortest_paths_FileName}.csv', 'Dijkstra'],
    ['floyd_shortest_paths_spl_matrix', f'{floydFileName}_spl.csv', 'Floyd'],
    ['floyd_shortest_paths_hops_matrix', f'{floydFileName}_hops.csv', 'Floyd'],
    ['floyd_shortest_paths_pmat_matrix', f'{floydFileName}_pmat.csv', 'Floyd'],
    ['betweenness_wei', 'NaN', 'Centrality'],
    ['agreement_wei', 'NaN', 'Clustering'],
    ['betweenness_bin', 'NaN', 'Clustering'],
    ['clustering_coef_wu', f'{clusCoefFileName}.csv', 'Clustering'],
    ['backbone_wu', 'NaN', 'Visualization'],
    ['rich_club', 'NaN', 'Vector of rich club coefficients'],
    ['NaN', 'NaN', 'NaN'],
    ['NaN', 'NaN', 'NaN']
]

# writing results to a csv file
with open(f'{res_path}algorithm_results.csv', 'w', encoding='UTF8', newline='') as f1:
    writer = csv.writer(f1)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)

with open(f'{res_path}algorithm_results.txt', 'w', encoding='UTF8', newline='') as f2:
    writer = csv.writer(f2)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)

# print(dir(bct))
