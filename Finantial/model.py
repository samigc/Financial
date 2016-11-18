##Highest:	523.88		Lowest: 381.25	Difference: 142.63	Average: 452.92	Change %: -13.02

import scipy.stats as stats
import pandas as pd
import re
import numpy as np
import json
from pprint import pprint

print("Hola mi corazón")
#http://www.investing.com/commodities/us-wheat-historical-data
#source (daily, 17 nov 2015- 17 nov 2016)
wheat = pd.read_csv('wheat.csv',sep = ';', names = [''])
with open("wheatjs.js") as wheatjs:
    wheat =  json.load(wheatjs)

pprint(wheat)
nombres = wheat["dataset"]["column_names"]
datos = wheat["dataset"]["data"]

print(nombres)
print(type(datos))


#print(js[0])
#print(type(js[0]))
#print(np.ndarray)
#print(np.matrix.sort(axis =1, order=js, ndarray='100' ))
#print(np.asarray(js))
#print(js)
