__author__ = 'rasheduzzaman'

import math
import random as rnd

def dot(W, X):
    res = [x * y for x, y in zip(W, X)]
    return sum(res)

def sigmoid_function(W, x):
    prob = 1.0 / (1 + math.exp(-dot(W, x)))
    if(prob >= 1.0):
        prob = 0.999999
    return prob

def normalize(ws):
    """Returns normalized set of weights that sum to 1."""
    s = sum(ws)
    return [float(w/s) for w in ws]



def cost_function(W, x, y):
    #cost = sum([(-y[i][0] * math.log(sigmoid_function(W, x[i]))) - ((1-y[i][0]) * math.log(1 - sigmoid_function(W, x[i]))) for i in range(0, len(x))])
    #cost = sum([math.log( 1 + math.exp(-1 * (y[i][0] * dot(W, x[i])))) for i in range(0, len(x))])
    cost = sum([(y[i][0] - math.log(1 + math.exp(-1 * dot(W, x[i]))))**2 for i in range(0, len(x))])
    return cost

def gradient_descent(data, labels, lrate = 0.01, esp = 1e-3, max_iter = 100000):
    val = X = [rnd.random() for i in range(0, len(data[0]))]
    W = normalize(val)
    converged = False
    J = cost_function(W, data, labels)
    iter = 0
    while not converged:
        pdict = [(sigmoid_function(W, data[i]) - labels[i][0]) for i in range(0, len(data))]
        temp=[[(data[i][j]*pdict[i]) for j in range(0,len(data[0]))] for i in range(0,len(data))]

        grad =  [sum(l) for l in zip(*temp)]

        W = [(W[i] - (lrate * grad[i])) for i in range(0, len(W))]

        error = cost_function(W, data, labels)
        if abs(J - error) < esp:
            print('Iteration: ', iter)
            converged = True
        J = error
        iter += 1
        if iter == max_iter:
            print('Iteration: ', iter)
            converged = True
    return W

if __name__ == '__main__':
    file_name_data = './data.txt'
    file_name_labels = './label.txt'
    data_set = open(file_name_data, 'r')
    labels_set = open(file_name_labels, 'r')

    data = [line.split() for line in data_set]
    data = [[int(column) for column in row] for row in data]
    for i in range(0, len(data)):
        data[i].append(1)

    labels = [line.split() for line in labels_set]
    labels = [[int(column) for column in row] for row in labels]

    W = gradient_descent(data, labels)
    W0 = W[len(W)-1]
    W = W[:2]
    magnitude = math.sqrt(sum([W[i]**2 for i in range(0, len(W))]))
    print(W)
    print(abs(W0/magnitude))
    print(magnitude)
