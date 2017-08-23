import csv
with open('oneID.csv','w',newline='') as csvfile1:
	spamwriter = csv.writer(csvfile1)
	with open('df_id_train.csv',newline='') as csvfile2:
		spamreader = csv.reader(csvfile2)
		for row in spamreader:
			if(row[1]=='1'):
				spamwriter.writerow(row)
