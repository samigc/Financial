##Highest:	523.88		Lowest: 381.25	Difference: 142.63	Average: 452.92	Change %: -13.02

import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#trigo = pd.read_csv('LSE-WEAT.csv'
raw = pd.read_csv('wheat.csv',sep = ';', names = ['month','day','year','open','close', 'high', 'low', 'change', '1','2','3','4', '5','6','7'])

weat = raw.ix[:,:'change']
data = weat.ix[:,['month', 'open']]
nrow = data.shape[0]
timest = pd.date_range('17/11/2015', periods = nrow, freq = 'D')

#test = pd.DataFrame({'date': timest})
test = weat.set_index('date').join(timest)
#test = data.join(timest)

#acum = data.cumsum()
#plt.figure(); acum.plot(); plt.legend(loc= 'best')
#plt.show()

print(test)
print(type(test))


#print(js[0])
#print(type(js[0]))
#print(np.ndarray)
#print(np.matrix.sort(axis =1, order=js, ndarray='100' ))
#print(np.asarray(js))
#print(js)
