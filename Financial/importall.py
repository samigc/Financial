import pandas as pd
import urllib.request


alltickers = pd.read_csv('WIKI-datasets-codes.csv')
print(alltickers)
datasets = alltickers.ix[:,0]

for i, row in datasets.iteritems():
	print(i,row)

	baseurl = "https://www.quandl.com/api/v3/datasets/"
	finalurl = ".csv?api_key=Y4AwT-TnxC_aybNKccqd&collapse=none"
	tickersample = row
	mydata = urllib.request.urlopen(baseurl+tickersample+finalurl).read()
	to_write = open(tickersample+".csv","w")
	to_write.write(mydata.decode())
	to_write.close()
	print("success")
	
