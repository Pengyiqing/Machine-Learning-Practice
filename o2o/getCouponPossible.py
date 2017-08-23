import csv
from datetime import date,datetime
from collections import Counter
def str2date(s):
	dType = datetime.strptime(s,'%Y%m%d')
	d = date(dType.year,dType.month,dType.day)
	return d
with open('couponPossible.csv','w',newline='') as f1:
	writer1 = csv.writer(f1)
	with open('ccf_offline_stage1_train.csv',newline='') as f2:
		reader1 = list(csv.reader(f2))
		with open('couponID.csv',newline='') as f3:
			reader2 = csv.reader(f3)
			for row2 in reader2:
				count = 0
				positive = 0
				effective = 0
				c = Counter()
				for row1 in reader1:
					if(row2[0]==row1[2]):
						count += 1
						if(row1[5]!='null' and row1[6]!='null'):
							positive += 1
							deltaDay = str2date(row1[6])-str2date(row1[5])
							if(deltaDay.days<15):
								effective += 1
								c[row1[4]] = c[row1[4]] + 1
				newRow=[row2[0],count,positive,effective,c]
				writer1.writerow(newRow)
