import pandas as pd
def notAllNull(column,row):
	column_null = pd.isnull(column)
	null = column[column_null == True]
	if(len(null)==row):
		return False
	else:
	 	return True

f1 = pd.read_csv('blocks/id9.csv',header=None)
for i in f1.values:
	f2 = pd.read_csv('divide_9/%s_%s.csv'%(i[0],i[1]),header=None)
	f2[55] = f2[55].str.replace('月','')
	if(notAllNull(f2[56],len(f2.index))):
		f2[56] = f2[56].str.replace('月','')
	if(notAllNull(f2[58],len(f2.index))):
		f2[58] = f2[58].str.replace('月','')
	f2[68] = f2[68].str.replace('月','')
	f2.to_csv('divide_9/%s_%s.csv'%(i[0],i[1]),header=None,index=None)
