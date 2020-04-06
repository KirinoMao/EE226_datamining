import pandas as pd
import numpy as np

def pre_load_save():
    # load data
    # DIM_x x=0,1,2,...,99
    # PID
    origin_data = pd.read_csv('course1.csv')
    origin_mat = np.array(origin_data)[:, 1:]
    np.save('course1.npy',origin_mat)

def dist(vec1,vec2):
    return np.sqrt(sum(np.power(vec1-vec2,2)))


def createCent(data,k):
    d = data.shape[1]
    tmp = np.zeros((k,d))
    for j in range(d):
        minJ = min(data[:,j])
        ranJ = float(max(data[:,j])-minJ)
        tmp[:,j] = minJ + ranJ * np.random.rand(k)

    return tmp

def main():
    # pre_load_save()
    data = np.load("course1.npy")
    # print(data.shape)
    # print(data[0]) # (50000, 100)
    N = data.shape[0]
    k = 5
    # generate the random start points
    centriods = createCent(data,k)
    # print(centriods)

    cluster_D = np.zeros((N,2))

    loop_cnt = 0
    flag = True
    while flag:
        flag =False
        loop_cnt +=1
        # update the centriods
        new_cent = np.zeros((k, data.shape[1]))
        cnt = np.zeros(k)

        for i in range(N):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distIJ = dist(data[i],centriods[j])
                if distIJ<minDist:
                    minDist=distIJ
                    minIndex = j
            if cluster_D[i,0]!=minIndex:
                flag = True
            cluster_D[i,:] = minIndex,minDist**2
            cnt[minIndex] += 1
            new_cent[minIndex] += data[i]

        for i in range(k):
            for j in range(new_cent.shape[1]):
                centriods[i][j] = new_cent[i][j]*1.0 / cnt[i]

        print(loop_cnt)
        print(centriods[:,:10])

    np.save('centriods.npy',centriods)
    np.save('cluster_D.npy',cluster_D)

def category_it():
    centriods = np.load("centriods.npy")
    cluster_D = np.load("cluster_D.npy")

    maxDist = np.zeros(5)

    N = cluster_D.shape[0]

    for i in range(N):
        if cluster_D[i][1] > maxDist[int(cluster_D[i][0])]:
            maxDist[int(cluster_D[i, 0])] = cluster_D[i, 1]

    print(maxDist)
    # [4.65689107 4.17089356 4.93819354 5.55143208 5.55468786]
    # [3,4,2,1,0]

    rev = [1, 0, 2, 3, 4]
    fin = []

    for i in range(N):
        fin.append(int(rev[int(cluster_D[i][0])]))

    data1 = pd.DataFrame(fin)
    data1.to_csv('fin.csv')



if __name__ == '__main__':
    main()