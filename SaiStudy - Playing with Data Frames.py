import pandas as pd
import numpy as np


df = pd.read_csv('students.csv')
#print(df[['Name']])
#print 5 rows only
df1 = df.iloc[:5]
#print(df1)

#print columns by posistions
df2 = df.iloc[:,:1]
#print(df2)

#apply filters to dataframes
#print(df[df['Marks']==999999])

data_mart = pd.read_csv('bigmart_data.csv')
#drop na values
data_mart = data_mart.dropna(how="any")
#print(data_mart.head())
sorted_data = data_mart.sort_values(by="Item_Weight")
#print(sorted_data[:5])

#merging data frames
result = pd.concat([data_mart,sorted_data], keys=['X','Y','Z'])
#print(result)

#print only rows from first data frame
#result.loc('X')

#merge on a particulr id
res = pd.merge(data_mart,sorted_data, on='Item_Identifier', how='outer')

#apply function, to apply a function row_wise or column_wise
print(data_mart.apply(lambda x: x[0]))
print(data_mart.apply(lambda x: x[0],axis=1))
def clip_price(price):
    if price > 200:
        price = 200
    return price

print(data_mart["Item_MRP"].apply(lambda x: clip_price(x))[:5])

#Aggregate functions
price_by_item = data_mart.groupby('Item_Type')
#print(price_by_item.first())
print(price_by_item.Item_MRP.mean())

#crosstab & pivottable in Aggregate Functions
ctb = pd.crosstab(data_mart['Outlet_Size'],data_mart['Outlet_Location_Type'],margins=True)
print(ctb)
pvt = pd.pivot_table(data_mart, index=['Outlet_Establishment_Year'], values=['Item_Outlet_Sales'])
print(pvt)
pd.datetime.now()