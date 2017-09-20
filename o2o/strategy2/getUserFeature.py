import pandas as pd
import numpy as np
from datetime import date,datetime
f1 = pd.read_csv('offline.csv')
#0:用户总消费次数;1:领取优惠券次数；2：用户获得优惠券的核销次数；3:用户核销优惠券点总消费次数；4：用户领取优惠券的核销率，5：用户领取优惠券后15天内的核销率； 6-13：用户满0-30/30-100/100以上/打折券15天内的核销率及四种情况的比重；14-15:用户15天内核销优惠券的平均折率和方差；16-17：用户15天内核销优惠券中平均距离和方差;18-19：用户总消费的平均距离和方差；
f2 = pd.DataFrame(columns=[i for i in range(20)])
gs1 = f1.groupby('User_id')
td = pd.to_timedelta('15 days')
k=0
for g in gs1:
	df1 = g[1]
	l = []
	count0 = df1['Date'].count()
	l.append(count0)
	count1 = df1['Coupon_id'].count()
	l.append(count1)
	df2 = df1.dropna(subset=['Coupon_id','Date'])
	l.append(df2.shape[0])
	if(df2.shape[0]):
		l.append((df2.shape[0]/count0))
		l.append((df2.shape[0]/count1))
		df2.iloc[:,5]=pd.to_datetime(df2.iloc[:,5])
		df2.iloc[:,6]=pd.to_datetime(df2.iloc[:,6])
		df3 = df2[(df2['Date']-df2['Date_received'])<td]
		l.append((df3.shape[0]/count1))
		if(df3.shape[0]):
			df4 = df1.dropna(subset=['Coupon_id'])['Discount_rate'].str.split(':',expand=True)
			df4 = df4.astype(float)
#似乎df4可能没有key=1
			c6_a = df4[(df4[0]>1)&(df4[0]<31)].shape[0]
			c7_a = df4[(df4[0]>30)&(df4[0]<101)].shape[0]
			c8_a = df4[df4[0]>100].shape[0]
			c9_a = 0
			if(c6_a or c7_a or c8_a):
				c9_a = df4.shape[0]-df4[1].count()
			else:
				c9_a = df4.shape[0]
			df5 = df3['Discount_rate'].str.split(':',expand=True)
			df5 = df5.astype(float)
			c6 = df5[(df5[0]>1)&(df5[0]<31)].shape[0]
			c7 = df5[(df5[0]>30)&(df5[0]<101)].shape[0]
			c8 = df5[df5[0]>100].shape[0]
			if(c6 or c7 or c8):
				c9 = df5.shape[0]-df5[1].count()
			else:
				c9 = df5.shape[0]
			if(c6_a):
				l += [c6/c6_a,c6/df5.shape[0]]
			else:
			 	l +=[np.NaN,np.NaN]
			if(c7_a):
				l += [c7/c7_a,c7/df5.shape[0]]
			else:
			 	l +=[np.NaN,np.NaN]
			if(c8_a):
				l += [c8/c8_a,c8/df5.shape[0]]
			else:
			 	l +=[np.NaN,np.NaN]
			if(c9_a):
				l += [c9/c9_a,c9/df5.shape[0]]
			else:
			 	l +=[np.NaN,np.NaN]
			s1 = []
			if(c6 or c7 or c8):
				s1 = (1-df5.dropna()[1]/df5.dropna()[0]).append(df5[0][df5[1].isnull()])
			else:
				s1 = (1-df5[0]) 
			l += [s1.mean(),s1.std()]
			s2 = df3.iloc[:,4].dropna().astype(int)
			l += [s2.mean(),s2.std()]
			s3 = df1['Distance'][df1['Date'].notnull()].notnull().astype(int)
			l += [s3.mean(),s3.std()]
		else:
			l += [np.NaN for i in range(14)]
	else:
	   	l += [0,0,0]
	   	l += [np.NaN for i in range(14)]
	f2.loc[g[0]]=l
	print(k)
	k = k+1
f2.to_csv('userFeature.csv',header = None)
