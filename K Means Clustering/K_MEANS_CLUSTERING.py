import pandas as pd
import random
import math
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.txt', sep=" ", header=None, dtype='float')
data1 = df.values

data = []
data2 = []

for a1, b1 in data1:
    a = round(a1, 5)
    b = round(b1, 5)
    data.append((a, b))
    data2.append((a, b, 0))

sz = len(data)
k = int(input('Enter no. of cluster: '))

rand = random.sample(range(0, sz), k)
cent = []

for i in range(0, k):
    cent.append(data[rand[i]])
    '''cent.append(data[i])'''

'''cent.append(data[0])'''
'''cent.append(data[3])'''

cls1_x = []
cls1_y = []
cls2_x = []
cls2_y = []

def find_cluster(p, q, s, t):
    dis = ((p-s) * (p-s)) + ((q-t) * (q-t))
    dis = math.sqrt(dis)
    return dis

def find_min(result):
    res = sorted(result, key=itemgetter(1))
    return res

prev_cnt = []

while(True):
    temp_table = []
    cls = []

    my_dict = {}
    for i in range(0, k):
        my_dict[i] = [0, 0, 0]

    '''print('my dict: ')
    print(my_dict)'''

    for i, j in data:
        x = i
        y = j

        result = []
        for d in range(0, k):
            temp_cent = cent[d]
            a2 = temp_cent[0]
            b2 = temp_cent[1]
            dist = find_cluster(x, y, a2, b2)
            result.append((d, dist))

        result = find_min(result)
        temp_data = []
        for d in range(0, k):
            r = result[d]
            temp_data.append(r[1])

        ind_l = result[0]
        ind = ind_l[0]
        cls.append(ind+1)
        temp_data.append(ind+1)
        temp_table.append(temp_data)

        for d in range(0, k):
            temp_dict = my_dict[d]

            if d == ind:
                temp_dict[0] = temp_dict[0] + x
                temp_dict[1] = temp_dict[1] + y
                temp_dict[2] = temp_dict[2] + 1
                my_dict[d] = temp_dict

    '''print('My dict: ')
    print(my_dict)

    print('My table: ')
    print(temp_table)

    print('count: ')
    print(cls)'''

    new_cnt = []
    for d in range(0, k):
        new_cnt.append(cls.count(d+1))

    '''print('prev count: ', prev_cnt)
    print('new count: ', new_cnt)'''

    if prev_cnt == new_cnt:
        break

    else:
        temp_cent1 = []

        for d in range(0, k):
            temp_dict1 = my_dict[d]
            a = temp_dict1[0]
            b = temp_dict1[1]
            c = temp_dict1[2]
            temp_cent1.append((a/c, b/c))

        cent = temp_cent1
        prev_cnt.clear()
        prev_cnt = new_cnt


Title = 'K_Means Clustering For Cluster size = '
Title = Title + str(k)

plt.figure(figsize=(10, 10))
plt.title(Title, color='red', fontweight="bold")
plt.xlabel('x-axis', color='red', fontweight="bold")
plt.ylabel('y-axis', color='red', fontweight="bold")

colors = ['', 'red', '#128117', '#611302', '#7905d9', '#ec05b8', 'yellow', '#05ec9f']
markers = ['', '8', 'p', 'h', 'X', 's', 'o', 'D']

ok = []
for i in range(0, k+1):
    ok.append(0)

for i in range(0, sz):
    temp_print = data[i]

    if ok[cls[i]] == 0:
        labels = 'Class - '
        labels = labels + str(cls[i])
        plt.scatter(temp_print[0], temp_print[1], color=colors[cls[i]], marker=markers[cls[i]], label=labels)
        ok[cls[i]] = 1
    else:
        plt.scatter(temp_print[0], temp_print[1], color=colors[cls[i]], marker=markers[cls[i]])


plt.legend()
plt.show()
