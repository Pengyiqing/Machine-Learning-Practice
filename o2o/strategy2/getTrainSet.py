import pandas as pd
import numpy as np
f1 = pd.read_csv('offline.csv')
f2 = pd.read_csv('userFeature.csv',index_col=0)
f3 = pd.read_csv('merchartFeature.csv',index_col=0)
f1 = f1.dropna(subset=['Coupon_id'])
f1['Date_received'] = pd.to_datetime(f1['Date_received'].astype(int).astype(str))
d = f1['Date_received']
d_f = pd.concat([d.dt.day,d.dt.weekday],axis=1)
c = f1['Discount_rate'].dropna().str.split(':',expand=True)
c = c.astype(float)
c1 = (1-c.dropna()[1]/c.dropna()[0]).append(c[0][c[1].isnull()])
c2 = c[1].isnull().astype(int)
c_f = pd.concat([c2,c1,c.dropna()[0]],axis=1)
df = f1.dropna(subset=['Date'])
df['Date']=pd.to_datetime(df['Date'].astype(int).astype(str))
label = (df['Date']-df['Date_received']).dt.days
label[(label/15)<=1]=1
label[(label/15)>1] = 15/label[(label/15)>1]
result = pd.concat([f1,c_f,d_f,label],axis=1)
print(len(result))
result.columns = ['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Date','c1','c2','c3','day','weekday','label']
result['label'] = result['label'].fillna(0)
result['User_id']=result['User_id'].astype(int)
#result1 = pd.merge(result,f2,how='inner',left_on='User_id',right_on='a')
result1 = result.join(f2,on='User_id')
print(len(result1))
result2 = result1.join(f3,on='Merchant_id')
#result2 = pd.merge(result1,f3,how='inner',left_on = 'Merchant_id',right_on='A')
print(len(result2))
result2.drop(['User_id','Merchant_id','Coupon_id','Discount_rate','Date_received','Date','a','A'],axis=1).to_csv('train_1.csv',index=False,float_format='%.6f')
