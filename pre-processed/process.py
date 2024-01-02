# import pandas with shortcut 'pd' 
import pandas as pd 

# read_csv function which is used to read the required CSV file 
data = pd.read_csv('NOFLY.csv/NOFLY.csv') 

# drop function which is used in removing or deleting rows or columns from the CSV files 
data.drop(['POB', 'TYPE', 'PASSPORT/IDNUMBER', 'CITIZENSHIP'], inplace=True, axis=1) 

# display 
data.to_csv('nofly.csv')