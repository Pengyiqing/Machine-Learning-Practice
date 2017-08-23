import csv
with open('oneRecord.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile)
	with open('oneID.csv', newline='') as csvfile1:
		spamreader1 = csv.reader(csvfile1)
		with open('df_train.csv', newline='') as csvfile2:
			for row1 in spamreader1:
				k=0
				i=0
				amount=0.0
				spamreader2 = csv.reader(csvfile2)
				for row2 in spamreader2:
					i=i+1
					if(row1[0]==row2[1]):
						k=k+1
						if(row2[60]):
							amount=amount+float(row2[60])
				newRow=[row1[0],str(k),str(amount)]
				spamwriter.writerow(newRow)
