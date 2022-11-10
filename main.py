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



df = pd.read_excel("pokemonData.xlsx",)

# def typeOfPokemon(peram1):
#   output = df["Name"].where(df['Type 1' or 'Type 2' or 'Generation' or 'Legendary'] == peram1)
#   print(output.dropna())
# typeOfPokemon("Water")

def typeOfPokemon(peram1):
  output = df.loc[(df["Name"].where(df['Type 1'] == peram1)) | (df["Name"].where(df['Type 2'] == peram1 ])]
  print(output.dropna())
typeOfPokemon("Water")



