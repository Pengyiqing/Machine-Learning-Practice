import csv
with open('1.csv',newline='') as f:
	reader = list(csv.reader(f))
	k=0
	for i in range(3):
		for row in reader:
			k += 1
		print(k)

