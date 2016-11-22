import os
import pandas as pd
from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats.stats import pearsonr
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as rd
random = rd.random

def year2day(rate):
    return (pow(1+rate,1/365)-1)

def estandar(file):
    df = pd.read_csv("WIKI/"+ file)
    cambio = (df['Close'] - df['Open'])/df['Open']
    est = np.std(cambio)
    print(np.mean(cambio))
    print(year2day(0.38))

estandar("AAL.csv")

data = pd.read_csv("allregressions3")
data = data.set_index('File')
data = pd.concat([data['Oil'],data['Wheat'], data['Beta'] ],axis=1, join='inner')

#print(data)

fig = plt.figure()
axx = fig.add_subplot(111, projection='3d')
axx.scatter(xs = data['Oil'],ys=data['Wheat'],zs=data['Beta'])
plt.xlabel('Oil')
plt.ylabel('Wheat')
plt.ylabel('Beta')
diff = list()
for i, row in data.iterrows():
    diff.append( np.linalg.norm(np.subtract([-1,-1,0] , list(row))))
#print(diff)

diffs = pd.DataFrame(diff,index=data.index)
diffs.columns = ["dist"]
diffs = diffs.sort('dist')

#diffs.hist(bins=50)
#plt.show()
#print(diffs)


#print(random())
