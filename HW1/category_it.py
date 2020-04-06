import numpy as np
import pandas as pd

def dist(vec1,vec2):
    return np.sqrt(sum(np.power(vec1-vec2,2)))


# data = np.load("course1.npy")
centriods = np.load("centriods.npy")
cluster_D = np.load("cluster_D.npy")

maxDist = np.zeros(5)

N = cluster_D.shape[0]

for i in range(N):
    if cluster_D[i][1]>maxDist[int(cluster_D[i][0])]:
        maxDist[int(cluster_D[i,0])] = cluster_D[i,1]

print(maxDist)
# [4.65689107 4.17089356 4.93819354 5.55143208 5.55468786]
# [3,4,2,1,0]

rev = [1,0,2,3,4]
fin = []

for i in range(N):
    fin.append(int(rev[int(cluster_D[i][0])]))

data1 = pd.DataFrame(fin)
data1.to_csv('fin.csv')

