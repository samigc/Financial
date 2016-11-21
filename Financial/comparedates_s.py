import pandas as pd
from numpy import *
import math
import matplotlib.pyplot as plt
weat = pd.read_csv('wheat2.csv', sep =';', names = ['Date','Price','Close', 'High', 'Low', 'Change', '1','2','3','4', '5','6','7'] )
weat = weat.ix[:,:'Change']
otro = pd.read_csv('LSE-WEAT.csv')

weati = weat.set_index('Date')
otroi = otro.set_index('Date')
print(otroi)

otroi = otroi.reindex_like(weati).dropna(how="all")

wheat = weati['Price']
wheat.name = 'wheat'
otter = otroi['Price']
otter.name = 'otter'
compare = pd.concat([wheat,otter],axis=1, join='inner')


compare.plot()
plt.show()
