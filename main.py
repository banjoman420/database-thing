from operator import index
import os 
import sys 
import pandas as pd 
import openpyxl
import xlrd
import json
import csv
import numpy as np
import openpyxl
loop = True

pd.set_option('display.max_rows', None)

cols = [0,1,2,3]
df = pd.read_excel("pokemonData.xlsx", usecols=cols,)
convertToDict = (df.to_dict('records'))
faveList = []

# def typeOfPokemon(peram1):
#   output = df["Name"].where(df['Type 1' or 'Type 2' or 'Generation' or 'Legendary'] == peram1)
#   print(output.dropna())
# typeOfPokemon("Water")


# #search function
# inputMon = input('what type of pokemon would you like?').title()
# def condSearch(poketype):
#   filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
#   print(df.loc[filt].to_string(index=False))
# condSearch(inputMon)

# userinp = input('what is the name of the pokemon you wish to save')
# name_to_add = (df.loc[df['Name'] == userinp.title()].to_dict('list'))
# faveList.append(name_to_add)
# print(faveList)


# #pull singular values
# userinp = input('what is the name of the pokemon you wish to save')
# # output = (df['Name'] == userinp.title()) 
# print(df.loc[df['Name'] == userinp.title()].to_string(index=False))



while loop:
  print(
    '''
    1. Display all data
    2. Search for spacific data
    3. Sort the data 
    4. Add data to favourites list
    5. Remove data from favourits list
    6. Display favourites list
    '''
  )

  #input for cases 
  numPick = input("pick the number of your desired option: ")
  match numPick:
    #1. Display all data
    case "1":
      print(df.to_string(index=False))
    
    #2. Search for spacific type
    case "2":
      inputMon = input('what type of pokemon would you like?').title()
      def condSearch(poketype):
        filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
        print(df.loc[filt].to_string(index=False))
      condSearch(inputMon)

    #3. Sort the data 
    case "3":
      print(convertToDict)

    
    #4. Add data to favourites list
    case "4":
      billy = (next(item for item in convertToDict if item['Name'] == 'Froakie'))
      faveList.append(billy)
      print(billy)
    
    #5. Remove data from favourits list
    case "5":
      userinp = input('what is the name of the pokemon you wish to save')
      name_to_add = (df.loc[df['Name'] == userinp.title()].to_dict('list'))
      faveList.append(name_to_add)
      print(faveList)



    case "6":
      print("hello")








