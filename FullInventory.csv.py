#Name- Wasay Usmani
#ID- 1878157

import pandas as pd 
import numpy as np



#Csv headers were a bit missaligned so insted of importing pd.read_csv I decided to just make my own dict
FullInventory = ({
    'ItemID':[1167234,2390112.0,9034210.0,7346234.0,3001265.0,2347800.0,1009453.0],
    'Manufacturer name':['Apple', 'Dell', 'Dell', 'Lenovo', 'Samsung', 'Apple','Lenovo'],
    'ItemType':['phone','laptop', 'tower', 'laptop', 'phone', 'laptop', 'tower'],
    'Price':[1200,999.0, 799.0, 599.0, 534.0, 345.0, 239.0],
    'ServiceDate':['5/27/2023','7/2/2022', '9/1/2023', '10/1/2023', '2/1/2024', '12/1/2023', '12/2/2022'],
    'Damaged':['NaN', 'NaN', 'damaged', 'NaN', 'NaN', 'NaN', 'NaN']})

df = pd.DataFrame(FullInventory)


print(df)



df.to_csv('D:\FullInventory.csv')



dfmain = pd.read_csv('D:\FullInventory.csv')


dfmain.head()


dfmain[['ItemID', 'Manufacturer name']]




dfmain['ItemType']


#filtering columns in dfmain for Phone type
filter = (dfmain == 'phone').any()
df_test = df.loc[: , filter]



print(df_test)


#adding only elements with phone to Phone inventory 
PhoneInventory = dfmain.query("ItemType == 'phone'")




#PhoneInventory
PhoneInventory.head()


#adding only elements with laptop to LaptopInventory
LaptopInventory = dfmain.query("ItemType == 'laptop'")






LaptopInventory.head()





#adding only element with tower to elTowerInventory
TowerInventory = dfmain.query("ItemType == 'tower'")


TowerInventory.head()



print(type(dfmain.ServiceDate[0]))



#converting service date to datetime
dfmain['ServiceDate'] = pd.to_datetime(dfmain['ServiceDate'])





print(type(dfmain.ServiceDate[0]))





dfmain.sort_values(by='ServiceDate', inplace=True)
dfmain





PastServiceDateInventory = dfmain





#PastServiceDateInventory.csv
PastServiceDateInventory





DamagedInventory = dfmain.query("Damaged == 'damaged'")





#DamagedInventory.csv
DamagedInventory




PhoneInventory.to_csv('D:\PhoneInventory.csv')





LaptopInventory.to_csv('D:\LaptopInventory.csv')





TowerInventory.to_csv('D:\TowerInventory.csv')





DamagedInventory.to_csv('D:\DamagedInventory.csv')





PastServiceDateInventory.to_csv('D:\DamagedInventory.csv')







