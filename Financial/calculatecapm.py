import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr

weat = pd.read_csv('cleanwheat.csv')
otro = pd.read_csv('WIKI/AAPL.csv')
sp = pd.read_csv('NYSE_SPY.csv')


weati = weat.set_index('Date')
otroi = otro.set_index('Date')
spi = sp.set_index('Date')

otroi = otroi.reindex_like(weati).dropna(how = "all")
spi = spi.reindex_like(weati).dropna(how = 'all')

wheat = weati['Open']
wheat.name = 'wheat'
otter = otroi['Open']
otter.name = 'otter'
spopen = spi['Open']
spopen.name = 'spopen'

compare = pd.concat([wheat,spopen, otter ],axis=1, join='inner')
compare = compare.dropna()
#ra = rf + beta*(rm -rf)
years = 6.07
rf = 0.00384
rows = compare['spopen'].shape[0]
#FINDING beta
spindex = list()
for i in range(0,rows-1):
    spindex.append((compare['spopen'][i+1]-compare['spopen'][i])/compare['spopen'][i])
otterindex = list()
for i in range(0,rows-1):
    otterindex.append((compare['otter'][i+1]-compare['otter'][i])/compare['otter'][i])

#returnsp =
dif = compare['spopen'][0]-compare['spopen'][rows-1]
rm = (dif/years)/compare['spopen'][rows-1]

#test = [compare['spopen'].shape[0], compare['wheat'].shape[0], compare['otter'].shape[0]]
rho = np.cov(spindex, otterindex, ddof = 0)[0][1]
beta = rho/np.var(spindex)

print(beta)
ra = rf + beta*(rm -rf)
#test = Rho*(np.std(compare['spopen'])/ np.std(compare['wheat']))
test= ra
print(test)
print(type(test))
#compare.plot()
#plt.show()
