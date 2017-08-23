import csv
index = 0
count = 0
file_in = open("blocks/%d.csv" % index,'w',newline='')
with open('df_id_train.csv',newline='') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		count += 1
		csvwriter = csv.writer(file_in)
		csvwriter.writerow(row)
		if(count == 2000):
			file_in.close()
			count=0
			index = index+1
			file_in = open("blocks/%d.csv" % index,'w',newline='')
			
