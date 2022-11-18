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

cols = [0,1,2,3]
df = pd.read_excel("pokemonData.xlsx", usecols=cols)
faveList = []

#load list
def loadFave():
  file = open("data.txt", "r")
  data = json.load(file)
  file.close()
  return data

#save list
def saveFave(fileToSave):
  file = open("data.txt", "w")
  json.dump(fileToSave, file)
  file.close()



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
    
    #2. Search for spacific data
    case "2":
      inputMon = input('what type of pokemon would you like?').title()
      def condSearch(poketype):
        filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
        print(df.loc[filt].to_string(index=False))
      condSearch(inputMon)

    #3. Sort the data 
    case "3":
      print("hello")
    
    #4. Add data to favourites list
    case "4":
      userinp = input('what is the name of the pokemon you wish to save')
      # output = (df['Name'] == userinp.title()) 
      billy = (df.loc[df['Name'] == userinp.title()].to_csv(index=False,header=False)).strip()
      print(billy)
      faveList.append(billy)
      print(faveList)

      

    
    case "5":
      print("hello")

    case "6":
      print("hello")








