import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.txt', sep=" ", header=None, dtype='Int64')
data = df.values

data_cls1 = []
data_cls2 = []

total_cls1_x = 0
total_cls1_y = 0
total_cls2_x = 0
total_cls2_y = 0

for i in data:
    temp = i

    if temp[2] == 1:
        data_cls1.append((temp[0], temp[1]))

    else:
        data_cls2.append((temp[0], temp[1]))

for x, y in data_cls1:
    total_cls1_x += x
    total_cls1_y += y

for x, y in data_cls2:
    total_cls2_x += x
    total_cls2_y += y

cls1_mean_x = int(total_cls1_x / len(data_cls1))
cls1_mean_y = int(total_cls1_y / len(data_cls1))
cls2_mean_x = int(total_cls2_x / len(data_cls2))
cls2_mean_y = int(total_cls2_y / len(data_cls2))

cls1_mean = []
cls2_mean = []

cls1_mean.append(cls1_mean_x)
cls1_mean.append(cls1_mean_y)

cls2_mean.append(cls2_mean_x)
cls2_mean.append(cls2_mean_y)

plt.figure(figsize=(10, 10))
plt.title('K_MEAN Classifier', color='red')
plt.xlabel('x-axis', color='red')
plt.ylabel('y-axis', color='red')

plt.scatter(*zip(*data_cls1), color='blue', marker='^', label='Class - 1 (Train Data).')
plt.scatter(*zip(*data_cls2), color='red', marker='v', label='Class - 2 (Train Data).')

df2 = pd.read_csv('test.txt', sep=" ", header=None, dtype='Int64')
data2 = df2.values

test_cls1 = []
test_cls2 = []
cnt = 0

for i in data2:
    temp = i

    new_cls = np.array([temp[0], temp[1]])

    f1 = np.dot(new_cls, cls1_mean) - (0.5 * np.dot(cls1_mean, cls1_mean))
    f2 = np.dot(new_cls, cls2_mean) - (0.5 * np.dot(cls2_mean, cls2_mean))

    if f1 >= f2:
        test_cls1.append((temp[0], temp[1]))
        if temp[2] is 1:
            cnt += 1
    else:
        test_cls2.append((temp[0], temp[1]))
        if temp[2] is 2:
            cnt += 1

accuracy = (cnt / (len(test_cls1) + len(test_cls2))) * 100
print('Accuracy: ', accuracy, "%")

plt.scatter(*zip(*test_cls1), color='purple', marker='^', label='Class - 1 (Test Data).')
plt.scatter(*zip(*test_cls2), color='green', marker='v', label='Class - 2 (Test Data).')

mx = cls1_mean_x - cls2_mean_x
my = cls1_mean_y - cls2_mean_y

cons = -0.5*(np.dot(cls1_mean, cls1_mean) - np.dot(cls2_mean, cls2_mean))
x = np.arange(-10, 10, 0.1)
y = (mx*x + cons) / (-my)

plt.plot(x, y, label='Decision Boundary', color='yellow')
plt.legend()
plt.show()

