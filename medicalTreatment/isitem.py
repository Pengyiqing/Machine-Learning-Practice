import pandas as pd
f1 = pd.read_csv('items.csv',header=None)
f2 = pd.read_csv('items_test.csv',header=None)
f2[1]=0
n=0
k=0
for item_t in f2[0]:
	for item in f1[0]:
		if(item_t==item):
			f2[1][n]=1
			k += 1
	n += 1
print(k)
f2.to_csv('items_test.csv',header=None,index=None)
