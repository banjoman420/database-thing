import os 
import sys 
import pandas as pd 
import openpyxl
import xlrd
import json
import csv
import numpy as np
loop = True

pd.set_option('display.max_rows', None)

#loading info from .txt file
def loadSave():
  file = open("save.txt", "r")
  data = json.load(file)
  file.close()
  return data

def saveInfo(fileToSave):
  file = open("save.txt", "w")
  json.dump(fileToSave, file)
  file.close()

#variables 
cols = [1,2,3,11,12]
df = pd.read_excel("pokemonData.xlsx",usecols=cols)

newDfnames = df['Name'].tolist()
newDfType1 = df['Type 1'].tolist()


# saveIndex = newDfnames.index('Rhydon')
# print(saveIndex)
# print(newDfType1[120])

def typeOfPokemon(peram1):
  output = df["Name"].where(df['Type 1' or 'Type 2' or 'Generation' or 'Legendary'] == peram1)
  print(output.dropna())
typeOfPokemon("Water")





