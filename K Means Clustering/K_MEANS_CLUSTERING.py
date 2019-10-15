import pandas as pd
import random
import math
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.txt', sep=" ", header=None, dtype='float')
data1 = df.values

data = []

for a1, b1 in data1:
    a = round(a1, 5)
    b = round(b1, 5)
    data.append((a, b))

sz = len(data)
k = 2

rand = random.sample(range(0, sz), k)

cent1 = data[rand[0]]
cent2 = data[rand[1]]

a = cent1[0]; b = cent1[1]
a1 = cent2[0]; b1 = cent2[1]

cls1_cnt = 0; cls2_cnt = 0
cls1_x = []
cls1_y = []
cls2_x = []
cls2_y = []

while(True):
    temp_table = []
    cent1_x = 0; cent1_y = 0
    cent2_x = 0; cent2_y = 0
    cls = []

    for i, j in data:
        x = i
        y = j

        dist1 = ((x-a) * (x-a)) + ((y-b) * (y-b))
        dist1 = math.sqrt(dist1)

        dist2 = ((x-a1) * (x-a1)) + ((y-b1) * (y-b1))
        dist2 = math.sqrt(dist2)

        if dist1 <= dist2:
            temp_table.append((dist1, dist2, 1))
            cent1_x = cent1_x + x
            cent1_y = cent1_y + y
            cls.append(1)

        else:
            temp_table.append((dist1, dist2, 2))
            cent2_x = cent2_x + x
            cent2_y = cent2_y + y
            cls.append(2)

    ncls1_cnt = cls.count(1)
    ncls2_cnt = cls.count(2)

    if (ncls1_cnt == cls1_cnt) and (ncls2_cnt == cls2_cnt):

        for i in range(0, sz):
            cl = temp_table[i]
            c = cl[2]
            temp = data[i]
            m = temp[0]
            n = temp[1]
            if c == 1:
                cls1_x.append(m)
                cls1_y.append(n)
            else:
                cls2_x.append(m)
                cls2_y.append(n)

        break

    else:
        a = cent1_x/ncls1_cnt; b = cent1_y/ncls1_cnt
        a1 = cent2_x/ncls2_cnt; b1 = cent2_y/ncls2_cnt
        cls1_cnt = ncls1_cnt
        cls2_cnt = ncls2_cnt

plt.figure(figsize=(10, 10))
plt.title('K_MEAN CLUSTERING', color='red')
plt.xlabel('x-axis', color='red')
plt.ylabel('y-axis', color='red')

plt.scatter(cls1_x, cls1_y, color='red', marker='.', label='Class - 1.')
plt.scatter(cls2_x, cls2_y, color='green', marker='.', label='Class - 2.')
plt.legend()
plt.show()
