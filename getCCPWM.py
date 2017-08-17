import csv
from collections import Counter
from datetime import date,datetime
def str2date(s):
	dType = datetime.strptime(s,'%Y%m%d')
	d = date(dType.year,dType.month,dType.day)
	return d
with open('CCPossibleWM.csv','w',newline='') as fw1:
	writer1 = csv.writer(fw1)
	with open('ccf_offline_stage1_train.csv',newline='') as fr1:
		reader1 = list(csv.reader(fr1))
		with open('m_c_ID.csv',newline='') as fr2:
			reader2= csv.reader(fr2)
			n=0
			l=['null','0','1','2','3','4','5','6','7','8','9','10']
			for row2 in reader2:
				count = 0
				positive = 0
				effective = 0
				c = Counter()
				for row1 in reader1:
					if(row2[0]==row1[3] and row2[1]==row1[1]):
						count +=1
						if(row1[5]!='null' and row1[6]!='null'):
							positive += 1
							deltaDay = str2date(row1[6])-str2date(row1[5])
							if(deltaDay.days<15):
								effective += 1
								c[row1[4]] = c[row1[4]] + 1
								n += 1
				z=[]
				for label in l:
					if(c[label]):
						z.append(c[label])
					else:
						z.append(None)
				newRow=[row2[0],row2[1],count,positive,effective]+z
				writer1.writerow(newRow)
							
						
