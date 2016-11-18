import pandas as pd
test = pd.read_csv('LSE-WEAT.csv')
invweat = pd.read_csv('wheat.csv', sep = ';')
otro = pd.read_csv('WIKI/ABFS.csv')

invweat.describe()
invweat = invweat.ix[:,:'1.57']
print(test)
print(type(test))
#print(otro.describe())

#print(trigo[trigo.Date > '2010-10-10']['Date'])
