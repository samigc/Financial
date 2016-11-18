import pandas as pd
trigo = pd.read_csv('LSE-WEAT.csv')
otro = pd.read_csv('WIKI/ABFS.csv')

print(trigo.describe())
print(otro.describe())

print(trigo[trigo.Date > '2010-10-10']['Date'])

otro.reindex_like(trigo)

trigoi = trigo.set_index('Date')
otroi = otro.set_index('Date')