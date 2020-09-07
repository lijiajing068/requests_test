#import csv

import pandas as pd
#data=csv.reader(open(my_file,'r'),header=None)
data=pd.read_csv("D:\Python\Scripts\lvmama\cases\login_data.csv",encoding='gb18030')
df=pd.DataFrame(data)
print(df)
print("**********")
songs=df['songs']
print(songs[0])
print(songs[1])
#print(df.iloc[1,0])
print("**********")
for index,row in df.iterrows():
    print(row['songs'])
    print("------")

