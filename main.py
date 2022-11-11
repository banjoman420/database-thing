from operator import index
import os 
import sys 
import pandas as pd 
import openpyxl
# import xlrd
import json
import csv
import numpy as np
loop = True

pd.set_option('display.max_rows', None)


df = pd.read_excel("pokemonData.xlsx")



def typeOfPokemon(peram1):
  output = df["Name"].where(df['Type 1' or 'Type 2' or 'Generation' or 'Legendary'] == peram1)
  print(output.dropna())
typeOfPokemon("Water")


#search function
inputMon = input('what type of pokemon would you like?').title()
def condSearch(poketype):
  filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
  print(df.loc[filt].to_string(index=False))
condSearch(inputMon)


#pull singular values
userinp = input('what is the name of the pokemon you wish to save')
# output = (df['Name'] == userinp.title()) 
print(df.loc[df['Name'] == userinp.title()].to_string(index=False))

empArr = []
listOfNames = df['Name'].to_dict()
empArr.append(listOfNames[5])
print(empArr)

