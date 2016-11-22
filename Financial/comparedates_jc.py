import pandas as pd
from numpy import *
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats.stats import pearsonr
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def normalize(data):
    return (data - data.mean()) / (data.std())
weat = pd.read_csv('cleanwheat.csv')

otro = pd.read_csv('WIKI/CMG.csv')
oil = pd.read_csv('OIL_WTI.csv')


weati = weat.set_index('Date')
otroi = otro.set_index('Date')
oili = oil.set_index('Date')

oili.columns = ['Price']
otroi = otroi.reindex_like(weati).dropna(how="all")
print(oili)
oili = oili.reindex_like(weati).dropna(how="all")
print(oili)
wheat = weati['Price']
wheat.name = 'wheat'
otter = otroi['High']
otter.name = 'otter'
print(oili)
oiil = oili['Price']
oiil.name = 'oil'
compare = pd.concat([wheat,otter,oiil],axis=1, join='inner')

compare.plot()
plt.show()



production = pd.read_csv('norwhtproduction.csv')


compare = compare.dropna()
data = pd.concat([compare['oil'],compare['wheat']],axis=1,join="inner")
target = pd.Series(compare['otter'])
lin = LinearRegression()


print(target.describe())

ax = lin.fit(data.as_matrix(),target.as_matrix())
print(ax.coef_)
print(ax.residues_)

plt.scatter(x = data['oil'] , y = target)
plt.show()
plt.scatter(x = data['wheat'] , y = target)
plt.show()

data_norm = normalize(data)
target_norm = normalize(target)
data_norm.plot()
target_norm.plot()
plt.show()

fig = plt.figure()
axx = fig.add_subplot(111, projection='3d')
axx.scatter(xs = data['oil'],ys=data['wheat'],zs=target)
plt.show()
