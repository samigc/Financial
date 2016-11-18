import pandas as pd
from numpy import *
import math
import matplotlib.pyplot as plt

weat = pd.read_csv('wheat2.csv', sep =';', names = ['Date','Price','Close', 'High', 'Low', 'Change', '1','2','3','4', '5','6','7'] )
weat = weat.ix[:,:'Change']

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


compare.plot()
plt.show()



# uswt = pd.read_csv('USWHEAT.tsv',sep='\t')
# li = uswt['Date'][0].split('-')
# lt = []
# uswtdat = uswt['Date']
# for i,row in uswtdat.iteritems():
# 	print(i,row)
# 	li = row
# 	li = li.split('-')
# 	li = li[2]+'-'+li[0]+'-'+li[1]
# 	print(li)
# 	lt.append(li)

# se = pd.Series(lt)
# uswt['Date'] = se
>>>>>>> 37d1c798fa8254328fbe286ecf41ef65465fbedf
