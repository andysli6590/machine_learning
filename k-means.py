import sys
import math
import random as rnd
from collections import defaultdict
import csv

csv.register_dialect('pipes', delimiter=' ', escapechar='\n')

def distance(x, k):
    sm = sum([(m - n)**2 for m, n in zip(x, k)])
    return math.sqrt(sm)

def find_cluster(X, k):
    d = defaultdict(list)
    mn = []
    for i in range(0,len(X)):
        temp = []
        for j in range(0,len(k)):
            temp.append(distance(X[i], k[j]))
        idx = temp.index(min(temp))
        d[idx].append(X[i])
    for key in d:
        temp = d[key]
        mn.append([sum(l)/len(l) for l in zip(*temp)])
    return mn

def has_converged(old, new):
    return (set([tuple(a) for a in old]) == set([tuple(a) for a in new]))

def k_means(X, k):
    mu = rnd.sample(X, k)
    while True:
        mu_new = find_cluster(X, mu)
        if has_converged(mu, mu_new):
            mu = mu_new
            break
        mu = mu_new
    # assign appropriate cluster label to each sample
    f = open('label.txt', 'w')
    for i in range(0,len(X)):
        temp = []
        for j in range(0,len(mu)):
            temp.append(distance(X[i], mu[j]))
        idx = temp.index(min(temp))
        print(idx, i)
        f.write('{} {}'.format(idx, i))
        f.write("\n")
    f.close()
    return mu

if __name__ == '__main__':
    '''
    file_name = sys.argv[1]
    k = int(sys.argv[2])
    data = []
    f = open(file_name, 'r')
    reader = csv.reader(f, dialect='pipes')
    for rows in reader:
        if not rows:
            continue
        temp = []
        for col in rows:
            if col != '':
                temp.append(float(col))
        data.append(temp)
    f.close()
    '''
    # testing data
    N = 8000
    data = [(rnd.uniform(0, 10), rnd.uniform(0, 10), rnd.uniform(0, 10)) for i in range(N)]
    k=3

    mu = k_means(data, k)
    print(mu)
    print('Output is written in label.txt file!')
