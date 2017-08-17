import csv
with open('submission_3.csv','w',newline='') as fw1:
	writer1 = csv.writer(fw1)
#number of each distance lable of all effective coupon  
	nedlaec=[7260,39699,7080,2819,1458,1018,666,485,320,313,261,2045]
#number of each distance lable of all coupon
	nedlac=[106003,348179,143871,81279,54944,40542,31010,24658,19682,16404,13961,172749]
	d={'null':5,'0':6,'1':7,'2':8,'3':9,'4':10,'5':11,'6':12,'7':13,'8':14,'9':15,'10':16}
	with open('ccf_offline_stage1_test_revised.csv',newline='') as fr1:
		reader1 = csv.reader(fr1)
		with open('CCPossibleWM.csv',newline='') as fr2:
			reader2 = list(csv.reader(fr2))
			for row1 in reader1:
				possible = 0.0
				for row2 in reader2:
					if(row1[3]==row2[0] and row1[1]==row2[1] and row2[2]!='0'):
						l = d[row1[4]]
						if(row2[l]):
							possible = (int(row2[l])*nedlac[l-5])/(int(row2[2])*nedlaec[l-5])
						else:
						 	possible = (int(row2[3])*nedlac[l-5])/(int(row2[2])*63411)
						if(possible > 1):
							possible = 1.0
				newRow=[row1[0],row1[2],row1[5],possible]
				writer1.writerow(newRow)
