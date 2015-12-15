__author__ = 'rasheduzzaman'

import math

def dot(W, X):
    res = [x * y for x, y in zip(W, X)]
    return sum(res)

def cost_function(W,x, y):
    cost = sum([(dot(W, x[i]) - y[i][0])**2 for i in range(0, len(x))])
    return cost

def gradient_descent(data, labels, lrate = 0.001, esp = 0.001, max_iter = 1000):
    val = 1.0/len(data[0])
    W = [val for i in range(0, len(data[0]))]
    #W = [rnd.random(), rnd.random(),  rnd.random()]
    converged = False
    J = cost_function(W, data, labels)
    iter = 0
    while not converged:
        pdict = [(dot(W, data[i]) - labels[i][0]) for i in range(0, len(data))]

        temp=[[(data[i][j]*pdict[i])for j in range(0,len(data[0]))] \
                for i in range(0,len(data))]

        grad =  [sum(l) for l in zip(*temp)]

        weight = [(W[i] - lrate * grad[i]) for i in range(0, len(W))]
        W = weight

        error = cost_function(W, data, labels)

        if abs(J - error) <= esp:
            #print("Successfully converged!! %d", iter)
            converged = True
        J = error
        iter += 1
        if iter == max_iter:
            #print("Max iteration reached!!")
            converged = True
    return W

if __name__ == '__main__':
    file_name_data = "./data.txt"
    file_name_labels = "./label.txt"
    data_set = open(file_name_data, 'r')
    labels_set = open(file_name_labels, 'r')

    data = [line.split() for line in data_set]
    data = [[int(column) for column in row] for row in data]
    for i in range(0, len(data)):
        data[i].append(1)

    labels = [line.split() for line in labels_set]
    labels = [[int(column) for column in row] for row in labels]
    for i in range(0, len(labels)):
        if labels[i][0] == 0:
            labels[i][0] = -1

    W = gradient_descent(data, labels)
    print(W[:-1])
    W0 = W[len(W)-1]
    magnitude = math.sqrt(sum([W[i]**2 for i in range(0, len(W)-1)]))
    print(abs(W0/magnitude))
