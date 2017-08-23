import csv
with open('itemData.csv','a',newline='') as f1:
	writer1 = csv.writer(f1)
	for i in range(9):
		with open('itemData_%d.csv'%(i+1),newline='')as f2:
			reader1 = csv.reader(f2)
			for row in reader1:
				writer1.writerow(row)
