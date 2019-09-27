import numpy as np
import random as rand
import matplotlib.pyplot as plt

data = []
Y = []
cls1 = []
cls2 = []
Title = "none"

with open('train.txt', 'r') as f:
    for line in f:
        d = []
        data = line.split()
        a = float(data[0])
        b = float(data[1])
        c = float(data[2])

        d6 = float(1)

        if c == float(2):
            d.append((-1) * (a*a)), d.append((-1) * (b*b)), d.append((-1) * (a*b))
            d.append((-1) * a), d.append((-1) * b), d.append((-1) * d6)
            cls2.append((a, b))

        else:
            d.append((a*a)), d.append((b*b)), d.append((a*b))
            d.append(a), d.append(b), d.append(d6)
            cls1.append((a, b))

        Y.append(d)

print('Y is: ', Y)


plt.figure(figsize=(8, 8))
plt.title('Plotting class values')
plt.xlabel('x-axis', color='red')
plt.ylabel('y-axis', color='red')

plt.scatter(*zip(*cls1), color='red', marker='o', label='Train cls1')
plt.scatter(*zip(*cls2), color='green', marker='*', label='Train cls2')

plt.legend()
plt.show()

print('Press ''1'' to initialize weights with All 1..')
print('Press ''0'' to initialize weights with All 0..')
print('Press ''R'' to initialize weights with Random Value..')

''' Batch Process start '''
learning_rate = []
batch_process = []
const = 0.1
last_range = 1.1
rate_cnt = 1

alpha = rate_cnt * const

choice = input('\nEnter Your Choice: ')
print('choice: ', choice)

while last_range - alpha > float(0):

    W = []
    flag = 1

    for i in range(0, 6):
        if choice is '0':
            W.append(0)
            Title = 'Learning Rate with weight of all 0 values'
        elif choice is '1':
            W.append(1)
            Title = 'Learning Rate with weight of all 1 values'
        elif choice is 'R':
            rand.seed(0)
            rand_val = rand.randint(1, 10) / 10
            W.append(rand_val)
            Title = 'Learning Rate with weight of Random values'
        else:
            print('Please enter valid choice..')
            flag = 0
            break

    if flag is 0:
        break

    result = [0, 0, 0, 0, 0, 0]
    cnt = 0
    temp = []

    alpha = round(alpha, 2)
    learning_rate.append(alpha)
    it = 0

    for k in range(0, 200):
        it = it + 1
        cnt = 0
        temp = []

        for i in range(0, 6):
            y = np.array(Y[i])
            w = np.array(W)
            res = np.dot(y, w)

            if res <= 0:
                temp.append(Y[i])
                cnt = cnt + 1

        if cnt is 0:
            break

        for i in range(len(temp)):
            t = temp[i]
            temp1 = []

            for j in range(0, 6):
                sum = result[j] + t[j]
                temp1.append(sum)

            result = temp1

        temp2 = []
        for i in range(0, 6):
            t2 = W[i] + (alpha * result[i])
            temp2.append(t2)

        W = temp2
        print('Batch Process W: ', W)

    batch_process.append(it)
    rate_cnt = rate_cnt + 1
    alpha = rate_cnt * const


''' Single Process start '''
rate_cnt = 1
alpha = rate_cnt * const
single_process = []

while last_range - alpha > float(0):

    W = []
    flag = 1

    for i in range(0, 6):
        if choice is '0':
            W.append(0)
            Title = 'Learning Rate with weight of all 0 values'
        elif choice is '1':
            W.append(1)
            Title = 'Learning Rate with weight of all 1 values'
        elif choice is 'R':
            rand.seed(0)
            rand_val = rand.randint(1, 10) / 10
            W.append(rand_val)
            Title = 'Learning Rate with weight of all Random values'
        else:
            print('Please enter valid choice..')
            flag = 0
            break

    if flag is 0:
        break

    result = [0, 0, 0, 0, 0, 0]
    cnt = 0
    temp = []
    it = 0

    for k in range(0, 200):
        it = it + 1
        cnt = 0
        temp = []

        for i in range(0, 6):
            y = np.array(Y[i])
            w = np.array(W)
            res = np.dot(y, w)

            if res <= 0:
                cnt = cnt + 1
                t = Y[i]
                temp = []

                for j in range(0, 6):
                    sum = W[j] + (alpha * t[j])
                    temp.append(sum)
                W = temp
                print('Single Process W: ', W)

        if cnt is 0:
            break

    single_process.append(it)
    rate_cnt = rate_cnt + 1
    alpha = rate_cnt * const


print('\tCnt\t\tLearning Rate\tOne At a Time\tMany At a Time')
for i in range(0, len(learning_rate)):
    print('\t', i+1, end='')
    print('\t\t', learning_rate[i], end='')
    print('\t\t\t', single_process[i], end='')
    print('\t\t\t\t', batch_process[i])


index = np.arange(10)
bar_width = 0.2

plt.bar(index, single_process, bar_width, label='Single Process', color='blue')
plt.bar(index+bar_width, batch_process, bar_width, label='Batch Process', color='orange')
plt.xticks(index+bar_width, learning_rate)

plt.title(Title, color='red', fontweight="bold")
plt.xlabel('Learning Rate', color='red', fontweight="bold")
plt.ylabel('Number of Iterations', color='red', fontweight="bold")
plt.legend()
plt.show()
