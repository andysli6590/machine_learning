import random as rnd
import csv
import math
import subprocess
from operator import itemgetter


##########################-----pearson correlation coefficients-----#######################################
def pcc_scores(X, y, top):
    rows = len(X)
    cols = len(X[0])
    xstd = []
    num = []
    r = []
    idx = 0
    ymn = sum(y)/rows
    ystd = math.sqrt(sum([(ymn - y[i])**2 for i in range(0,rows)]))
    xmn = [sum(x)/rows for x in zip(*X)]
    for x in zip(*X):
        if idx != len(xmn):
            sm = nm = 0
            for i,j in zip(x,y):
                sm += (xmn[idx] - i)**2
                nm += (xmn[idx] - i)*(ymn-j)
            xstd.append(math.sqrt(sm))
            num.append(nm)
            idx +=1
    den = [ystd*xd for xd in xstd]
    for n,d in zip(num, den):
        if d == 0:
            r.append(0)
        else:
            val = n/d
            if val < 0:
                r.append(val*1)
            else:
                r.append(val)
    indices, v_sorted = zip(*sorted(enumerate(r), key=itemgetter(1), reverse=True))
    V = []
    cnt = 0
    for i in indices:
        if cnt < top:
            V.append(X[:,i])
        cnt +=1
    indices, v_sorted = zip(*sorted(enumerate(r), key=itemgetter(1)))
    cnt = 0
    for i in indices:
        if cnt < top:
            V.append(X[:,i])
        cnt +=1
    return V
