import csv
n=1
while(n<5):
	with open('blocks/id9.csv',newline='') as f1:
		reader1 = csv.reader(f1)
		with open('%d.csv' % n, newline='') as f2:
			reader2 = list(csv.reader(f2))
			for row1 in reader1:
				with open('divide_9/%s_%s.csv' % (row1[0],row1[1]),'a',newline='') as f3:
					writer1 = csv.writer(f3)
					for row2 in reader2:
						if(row1[0]==row2[1]):
							writer1.writerow(row2)
	n=n+1
