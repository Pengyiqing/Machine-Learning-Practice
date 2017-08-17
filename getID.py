import csv
from collections import Counter
with open('meID_train.csv','w',newline='') as f1:
	writer1 = csv.writer(f1)
	with open('ccf_offline_stage1_train.csv',newline='') as f2:
		c = Counter()
		reader1 = csv.reader(f2)
		for row in reader1:
			c[row[1]] = c[row[1]] + 1
		for i in c:
			newRow = [i,c[i]]
			writer1.writerow(newRow)
