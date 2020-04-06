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


'''
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxGaO4zmWqGKtyYxiNv2pKq4qMSUD0gy2JDBuwcQI076oVwxU
KNqL1oHQa11uNkxyEgMrZrDUT5HXlVUP1pjQ+dpkuvLwkN+mw5AgFUBKLv8w07r8
ef8rFUrHGedu3vPdeX0s9WTOBV5WBhY6qH78l1vXREKERQnAx38mqfPurk0619E9
a34ZnLtq4urSUI0U89Ha4QUlG9oIEVQ+v9w5PynqcIHRLbmoxm5MduExYxOFVR2f
V7RUUAmhasIxpfZFjo1BpA3BHg+BWig6akfymqgWhkgv2cReSBRRItPllwpkqqaQ
4itcbGVo6ZhYWN3/MS8Fu1gPH8JV2ra4NIjWxQIDAQABAoIBAFsDM7/0le5eHC7E
EVduYRBYOVEg2A5kuZs3nnvIflaxiY0dN3rfG+JBsfWvDD25WzshoOErnJdq/D5F
dtt5YY4HOJqxre1U1xDVHyj56+avd08G3a0jJDHvvygv6V8EH2QHL+hf2GEAgFi9
wF0Iy8DQXIdTU7wyctWABMjJM5gtfe/70v/fesKYPy6EOjyGazDbo4Dt/5WwlT8p
QJduolpwdAPaMiMYUC0BEiFnWSwz2XkXOiokUi7caOsspCkFbt0D9VfbT0orw4sU
bSDLtobNX90rrA/XXcQt2nXglTvfWiBBL1IaQ+lZAchjonyC5X049I5GYGEdgUb3
TrM1QJkCgYEA5bLLhtQGOYm53s5tkJmWrrgj1iEDMIYq6W/TeTotiUGb5o4CW5Xv
115DL6MAzWp3ffeiu6I/Wkdr2kiNk0JheDrrQJr9CcdK4FtE06CKUehFGcmgYbeN
3m9Ihk0+kkzqcc1cpnEUChE8O1skKRnShdbwPxEWCBK3EwRWIB+ACL8CgYEA2uOy
WveKzWTltx0tMCzd9OGLwi/aTJ+pu9uPcNXARd9am+oQ0MVe303kWM6aqGvhhfMU
H/efl8VcnuUyjPoMiKhBvNOVeBbdVFCi9zTjR2zpoeW+gOhouZM01XDToDqgbd59
09LGLjKGBsCyo4lhVeoY3NLuIgd7SLvnd4G5HXsCgYArai7jzgFbMLfr7/JviUgc
v/suBtFWg5Vqx9Mdr6xZrAfufNrfOqi5eTyTrWiCauQo7/xXIKR+yM8O0/XGZp6L
nf9HF8RJ69wwKbAJm+do8dDVvfFNZucuqrP3hnQULOuHFPy1DNxvxrAuu9xK1HGh
EG4aTX1vizIFKyWoLqwBewKBgFMmrFpiLxhXe+xT6Raj9K1SAQWDqCnzfUcf4R28
FY51irYv9LNaRvANZvFViurwEHwSG1MJflbpYoX6C3oCg0BmqpJQzjcQeIPPHhlK
vgwkE5ys6fGOWDom8asjcUEtBES4gJQ3PZHPH5rxGOuHBLLeexNoDY5fyTWYLBX5
8ZiBAoGAETZbZx9vTCI6FF8l7RlCB42SKAo5hLHTVsI9DVxx9MMVEkYcnpwWyEWJ
+n9kKnlAFA/s3YUlmao9drTg5MfuzMVDANDYhSaJuyCm1BvXsavgnkbFFpBAowom
LaOpxYTIgZBYnBLozSNI4bHJ1mPJGubjclVSQJCMP11Hn21YvtA=
-----END RSA PRIVATE KEY-----

'''