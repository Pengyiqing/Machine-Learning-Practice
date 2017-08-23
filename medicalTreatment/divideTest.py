import csv
with open('df_id_test.csv',newline='') as f1:
	reader1 = csv.reader(f1)
	with open('df_test.csv', newline='') as f2:
		reader2 = list(csv.reader(f2))
		for row1 in reader1:
			with open('test/%s.csv' % row1[0],'w',newline='') as f3:
				writer1 = csv.writer(f3)
				for row2 in reader2:
					if(row1[0]==row2[1]):
						writer1.writerow(row2)

