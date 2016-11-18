import pandas as pd
test = pd.read_csv('LSE-WEAT.csv')
invweat = pd.read_csv('wheat.csv', sep = ';')
otro = pd.read_csv('WIKI/ABFS.csv')

print(trigo[trigo.Date > '2010-10-10']['Date'])

otro.reindex_like(trigo)

trigoi = trigo.set_index('Date')
otroi = otro.set_index('Date')

