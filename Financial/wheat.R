
wheat = read.csv("wheat.csv",sep = ';')
wheat = raw[,1:8]
(wheat)
raw = read.csv("wheat.csv", sep = ';', col.names = c('month','day', 'year','open','close', 'high', 'low', 'change', '1','2','3','4', '5','6','7'))
wheat = raw[,1:8]
#ordering data as a time-series, oldest to newest
wheat[with(wheat, order(year, month)), ]
levels(wheat$month)
month.nameabr = substr(month.name, 1, 3)
m_fac = factor(wheat$month, levels=month.nameabr)
wheato = wheat[with(wheat, order(year, m_fac, day)),]

#create a plot showing variance of prices, with splines.
wheato$delta = wheato$close - wheato$open
wheato$change*
wheato[,8:9]
ggplot2()
