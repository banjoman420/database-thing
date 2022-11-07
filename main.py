import os 
import sys 
import pandas as pd 


#variables 
cols = [1,2,3]
df = pd.read_excel("pokemonData.xlsx",usecols=cols)
# print(df)

for n in df:
    print(n)