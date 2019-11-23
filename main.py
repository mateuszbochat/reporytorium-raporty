import pandas as pd 
transactions = pd.read_csv('raport.csv', sep=';', index_col=None)
print(transactions.head())