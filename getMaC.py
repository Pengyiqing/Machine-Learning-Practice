import csv
with open('m_c_ID.csv','w',newline='') as fw1:
	writer1 = csv.writer(fw1)
	with open('couponContent.csv',newline='') as fr1:
		reader1 = csv.reader(fr1)
		with open('ccf_offline_stage1_test_revised.csv',newline='') as fr2:
			reader2 = list(csv.reader(fr2))
			for row1 in reader1:
				s = set()
				for row2 in reader2:
					if(row1[0] == row2[3]):
						s.add(row2[1])
				for i in s:
					newRow=[row1[0],i]
					writer1.writerow(newRow)
