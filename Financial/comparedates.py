import pandas as pd
weat = pd.read_csv('LSE-WEAT.csv')
otro = pd.read_csv('WIKI/ABFS.csv')


#otro.reindex_like(trigo)

weati = weat.set_index('Date')
otroi = otro.set_index('Date')

otroi = otro.reindex_like(weati).dropna(how="all")