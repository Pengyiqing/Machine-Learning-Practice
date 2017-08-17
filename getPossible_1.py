import csv
with open('submission_2.csv','w',newline='') as fw1:
	writer1 = csv.writer(fw1)
#number of each distance lable of all effective coupon  
	nedlaec=[7254,39697,7078,2819,1457,1017,666,485,320,313,261,2044]
#number of each distance lable of all coupon
	nedlac=[106003,348179,143871,81279,54944,40542,31010,24658,19682,16404,13961,172749]
	d={'null':4,'0':5,'1':6,'2':7,'3':8,'4':9,'5':10,'6':11,'7':12,'8':13,'9':14,'10':15}
	with open('ccf_offline_stage1_test_revised.csv',newline='') as fr1:
		reader1 = csv.reader(fr1)
		with open('contentPossible.csv',newline='') as fr2:
			reader2 = list(csv.reader(fr2))
			for row1 in reader1:
				possible = 0.0
				for row2 in reader2:
					if(row1[3]==row2[0] and row2[1]!='0'):
						l = d[row1[4]]
						if(row2[l]):
							possible = (int(row2[l])*nedlac[l-4])/(int(row2[1])*nedlaec[l-4])
						else:
						 	possible = (int(row2[3])*nedlac[l-4])/(int(row2[1])*63411)
						if(possible > 1):
							possible = 1.0
				newRow=[row1[0],row1[2],row1[5],possible]
				writer1.writerow(newRow)
