import csv
with open ('11record.csv','w',newline='') as csvfile1:
	spamwriter = csv.writer(csvfile1)
	with open('df_train.csv',newline='') as csvfile2:
		spamreader = csv.reader(csvfile2)
		for row in spamreader:
			if(row[1]=='352120001187177'):
				spamwriter.writerow(row)
