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

#Go for all the files
#Get the regression coefficients for this file and the oil / wheat
#Save as csv
files = pd.Series(os.listdir('WIKI'))
print(files)
wheat = pd.read_csv('cleanwheat.csv')
oil = pd.read_csv('OIL_WTI.csv')
wheati = wheat.set_index('Date')
oili = oil.set_index('Date')
oili.columns = ['Oil']
wheati = wheati['Price']
wheati.name = 'Wheat'
print(wheati)
print(oili)

def getLinearCoefficients(a1,a2,y):
    #Enter 3 series with their times
    alldata = pd.concat([a1,a2,y],axis=1,join="inner").dropna()
    data = pd.concat([alldata['Oil'],alldata['Wheat']],axis=1,join="inner")
    target = pd.Series(alldata['Asset'])
    lin = LinearRegression()
    ax = lin.fit(data.as_matrix(),target.as_matrix())
    print(ax.coef_)
    return(ax.coef_)

#Get the first file

allrelations = pd.DataFrame(columns=['File','Oil','Wheat'])

for i, row in files.iteritems():
    ff = pd.read_csv('WIKI/'+row)
    ff = ff.set_index('Date')
    newf = ff['High']
    newf.name = 'Asset'
    print(i,row)
    mlcoef = getLinearCoefficients(wheati,oili,newf)
    allrelations = allrelations.append({'File': row,'Oil' : mlcoef[0], 'Wheat' : mlcoef[1]}, ignore_index=True)
    #print(allrelations)

allrelations.to_csv('allregressions.csv')
