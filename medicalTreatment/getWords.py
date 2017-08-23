import csv
import re
def numover3(s):
	if(s):
		k=0
		for i in s:
			if(str.isdigit(i)):
				k=k+1
		if(k<4):
			return False
		else:
		 	return True
	else:
	  	return False
with open('items_test.csv','w',newline='') as f1:
	writer1 = csv.writer(f1)
	with open('df_test.csv',newline='') as f2:
		s1 = set()
		reader1 = csv.reader(f2)
		for row in reader1:
			if(row[59]):
				for w2 in re.split(r',|:|\s|;|合并|病|症|;|@|（|）|，|、|；|：|合併|伴|。',row[59]):
					s1.add(w2)
		s2 =set()
		s1.remove('')
		for w3 in s1:
			if(numover3(w3)):
				w4=''
				for c in filter(str.isalpha,w3):
					w4 = w4+c
				s2.add(w4)
			else:
				s2.add(w3)
		s2.remove('')
		for i in s2:
			writer1.writerow([i])
