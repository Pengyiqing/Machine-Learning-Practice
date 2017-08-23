import csv
with open('oneRecord_all_4.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile)
	with open('df_id_train.csv', newline='') as csvfile1:
		spamreader1 = csv.reader(csvfile1)
		with open("4.csv", newline='') as f_use:
			spamreader2 = list(csv.reader(f_use))
			for row1 in spamreader1:
				k=0
				amount=0.0
				for row2 in spamreader2:
					if(row1[0]==row2[1]):
						k=k+1
						if(row2[60]):
							amount=amount+float(row2[60])
				newRow=[row1[0],row1[1],str(k),str(amount)]
				spamwriter.writerow(newRow)
