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
wheat = pd.read_csv('cleanwheat.csv')
oil = pd.read_csv('OIL_WTI.csv')
wheati = wheat.set_index('Date')
oili = oil.set_index('Date')
oili.columns = ['Oil']
wheati = wheati['Price']
wheati.name = 'Wheat'
sp = pd.read_csv('NYSE_SPY.csv')
spi = sp.set_index('Date')
spopen = spi['Open']
spopen.name = 'spopen'
years = 6.07
rf = 0.00384


def getLinearCoefficients(a1,a2,a3,y):
    #Enter 3 series with their times
    alldata = pd.concat([a1, a2, a3 ,y ], axis = 1, join = "inner" ).dropna()
    data = pd.concat([alldata['Oil'],alldata['Wheat']],axis=1,join="inner")
    target = pd.Series(alldata['Asset'])
    lin = LinearRegression()
    ax = lin.fit(data.as_matrix(),target.as_matrix())
    rows = alldata['spopen'].shape[0]
    spindex = list()
    for i in range(0,rows-1):
        spindex.append((alldata['spopen'][i+1]-alldata['spopen'][i])/alldata['spopen'][i])
    Assetindex = list()
    for i in range(0,rows-1):
        Assetindex.append((alldata['Asset'][i+1]-alldata['Asset'][i])/alldata['Asset'][i])
    dif = alldata['spopen'][0]-alldata['spopen'][rows-1]
    rm = (dif/years)/alldata['spopen'][rows-1]
    rho = np.cov(spindex, Assetindex, ddof = 0)[0][1]
    beta = rho/np.var(spindex)
    ra = rf + beta*(rm -rf)
    betara = list(ax.coef_) + [beta,ra]
    return(betara)


allrelations = pd.DataFrame(columns=['File','Oil','Wheat','Beta', 'Return'])

for i, row in files.iteritems():
    ff = pd.read_csv('WIKI/'+row)
    ff = ff.set_index('Date')
    newf = ff['High']
    newf.name = 'Asset'
    mlcoef = getLinearCoefficients(wheati,oili,spopen,newf)
    print(i,row,mlcoef)
    allrelations = allrelations.append({'File': row,'Oil' : mlcoef[0], 'Wheat' : mlcoef[1], 'Beta' : mlcoef[2], 'Return' : mlcoef[3]}, ignore_index=True)
    #print(allrelations)

allrelations.to_csv('allregressions2.csv')
