import pandas as pd
from numpy import *
import math
import matplotlib.pyplot as plt

weat = pd.read_csv('cleanwheat.csv')

otro = pd.read_csv('WIKI/ABFS.csv')
print(weat)

weati = weat.set_index('Date')
otroi = otro.set_index('Date')


otroi = otroi.reindex_like(weati).dropna(how="all")


wheat = weati['Price']
wheat.name = 'wheat'
otter = otroi['High']
otter.name = 'otter'
compare = pd.concat([wheat,otter],axis=1, join='inner')

#compare.plot()
#plt.show()

from scipy.stats.stats import pearsonr
pearsonr(compare['wheat'],compare['otter'])


production = pd.read_csv('norwhtproduction.csv')
print(production['Volume (Tons)'].sum())