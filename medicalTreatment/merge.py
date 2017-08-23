import csv
with open("oneRecord_all.csv",'w',newline='') as f:
	swriter = csv.writer(f)
	with open("oneRecord_all_1.csv",newline='') as cf_1, open("oneRecord_all_2.csv",newline='') as cf_2, open("oneRecord_all_3.csv",newline='') as cf_3, open("oneRecord_all_4.csv",newline='') as cf_4:
		r1 = csv.reader(cf_1)
		r2 = csv.reader(cf_2)
		r3 = csv.reader(cf_3)
		r4 = csv.reader(cf_4)
		for row1, row2, row3, row4 in zip(r1,r2,r3,r4):
			newcount = str(int(row1[2])+int(row2[2])+int(row3[2])+int(row4[2]))
			newamount = str(float(row1[3])+float(row2[3])+float(row3[3])+float(row4[3]))
			newrow = [row1[0],row1[1],newcount,newamount]
			swriter.writerow(newrow)
