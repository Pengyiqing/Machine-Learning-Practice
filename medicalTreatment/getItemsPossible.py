import pandas as pd
import re
from collections import Counter
def numover3(s):
	if(s):
		k=0
		for i in s:
			if(str.isdigit(i)):
				k=k+1
		if(k<4):
			return False
		else:
		 	return True
	else:
	  	return False

f1 = pd.read_csv('blocks/id9.csv',header=None)
f2 = pd.read_csv('items.csv',header=None)
f3 = pd.DataFrame(columns=['label']+list(f2[0]))
l1 = len(f2.index)
z=0
for i in f1.values:
	f4 = pd.read_csv('divide_9/%s_%s.csv'%(i[0],i[1]),header=None)
	f3.loc[z] = [int(i[1])]+[int(0) for n in range(l1)]
	c = Counter()
	l2 = len(f4.index)
	datas = pd.Series(f4[59]).dropna()
	for w1 in datas:	
		for w2 in re.split(r',|:|\s|;|合并|病|症|;|@|（|）|，|、|；|：|合併|伴|。',w1):
			if(numover3(w2)):
				w3=''
				for x in filter(str.isalpha,w2):
					w3 = w3+x
				c[w3] = c[w3]+1
			else:
			  	c[w2] = c[w2]+1
	del c['']
	for w4 in c:
		f3[w4][z] = c[w4]/l2
	z = z+1
f3.to_csv('itemData_9.csv',index=0)
