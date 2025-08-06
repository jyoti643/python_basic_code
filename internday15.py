import pandas as pd
dF=pd.read_csv(r"C:\Users\Jyoti Shekhawat\OneDrive\Desktop\sales_data_sample.csv",encoding='latin1')
# print(dF.sample(10))
# print(dF.index)
# print(dF.values)
# print(dF[["CITY","CUSTOMERNAME"]])
# print(dF.iloc[5:10])
# print(dF.loc[dF["CITY"]=='Paris'])
# print(dF[dF['PRICEEACH'] > 70])            # Employees with salary > 70K
# print(dF[dF['YEAR_ID'] == 2004])         # All HR employees
dF['STATUSPOSITION']='ACTIVE'
print(dF)