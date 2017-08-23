import csv
import re
with open('items_1.csv','w',newline='') as f1:
	writer1 = csv.writer(f1)
	with open('items.csv',newline='') as f2:
		s1 = set()
		reader1 = csv.reader(f2)
		for row in reader1:
			if(row[0]):
				for w2 in re.split(r'，|、|：|；|@',row[0]):
					s1.add(w2)
		s1.remove('')
		print(len(s1))
		for i in s1:
			writer1.writerow([i])
