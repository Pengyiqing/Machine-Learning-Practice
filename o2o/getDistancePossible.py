import csv
from datetime import date,datetime
from collections import Counter
def str2date(s):
	dType = datetime.strptime(s,'%Y%m%d')
	d = date(dType.year,dType.month,dType.day)
	return d
with open('distancePossible.csv','w',newline='') as f1:
	writer1 = csv.writer(f1)
	with open('ccf_offline_stage1_train.csv',newline='') as f2:
		reader1 = list(csv.reader(f2))
		n=0
		distances = ['null','0','1','2','3','4','5','6','7','8','9','10']
		for d in distances:
			count = 0
			positive = 0
			effective = 0
			for row1 in reader1:
				if(row1[2]!='null' and d==row1[4]):
					count += 1
					if(row1[5]!='null' and row1[6]!='null'):
						positive += 1
						deltaDay = str2date(row1[6])-str2date(row1[5])
						if(deltaDay.days<15):
							effective += 1
							n += 1
			newRow=[d,count,positive,effective]
			writer1.writerow(newRow)
		print(n)
