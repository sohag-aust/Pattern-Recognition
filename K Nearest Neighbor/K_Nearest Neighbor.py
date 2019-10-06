import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('train.txt', sep=",", header=None)
data1 = df1.values

train_data = []
x1 = []
y1 = []
x2 = []
y2 = []

for a,b,c in data1:
    train_data.append((a,b,c))

    if c == 1:
        x1.append(a)
        y1.append(b)
    else:
        x2.append(a)
        y2.append(b)

df2 = pd.read_csv('test.txt', sep=",", header=None)
data2 = df2.values

result = []

KN = int(input('Enter no. of neighbor: '))

def find_min(result):
    res = sorted(result, key=itemgetter(0))
    return res

predict_x1 = []
predict_x2 = []
predict_y1 = []
predict_y2 = []

with open("predict.txt", "w") as file:
    for a,b in data2:
        file.write("Test Point: ")
        file.write(str(a)+","+str(b)+"\n")

        result = []
        for i in train_data:
            dist = ((i[0]-a)*(i[0]-a)) + ((i[1]-b)*(i[1]-b))
            result.append((dist, i[2]))

        result = find_min(result)
        result = result[:KN]
        temp = []

        for j in result:
            temp.append(j[1])

        cls1 = temp.count(1)
        cls2 = temp.count(2)

        predict = 0

        if cls1 > cls2:
            predict = 1
            predict_x1.append(a)
            predict_y1.append(b)
        elif cls1 < cls2:
            predict = 2
            predict_x2.append(a)
            predict_y2.append(b)

        cnt = 1
        for key,value in result:
            file.write("Distance "+str(cnt)+": "+str(key)+"\t"+"Class: "+str(value)+"\n")
            cnt += 1

        if predict is 0:
            file.write("This point is supposed to both class"+"\n\n")
        else:
            file.write("Predicted class: "+str(predict)+"\n\n")

plt.figure(figsize=(10, 10))
plt.title('K_MEAN Classifier', color='red')
plt.xlabel('x-axis', color='red')
plt.ylabel('y-axis', color='red')
plt.scatter(x1, y1, color='blue', marker='^', label='Class - 1 (Train Data).')
plt.scatter(x2, y2, color='red', marker='v', label='Class - 2 (Train Data).')
plt.scatter(predict_x1, predict_y1, color='green', marker='^', label='Predicted Class-1.')
plt.scatter(predict_x2, predict_y2, color='black', marker='v', label='Predicted Class-2.')
plt.legend()
plt.show()
