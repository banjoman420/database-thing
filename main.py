from operator import index
import pandas as pd 
import openpyxl
import xlrd
import json
import numpy as np
import openpyxl
loop = True

pd.set_option('display.max_rows', None)

cols = [0,1,2,4,3,6,8,10]
df = pd.read_excel("pokemonData.xlsx", usecols=cols)
convertToDict = (df.to_dict('records'))
faveList = []


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

def selectionSort(anArray, whatToSearch):
    for fill_slot in range(len(anArray)):
        min_position = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if anArray[post_fill][whatToSearch] < anArray[min_position][whatToSearch]:
                min_position = post_fill

        anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]

def printCase3(searchBy):
  selectionSort(copy_to_disp, searchBy)
  for i in range(len(copy_to_disp)):
    print(copy_to_disp[i])



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
      copy_to_disp = (convertToDict.copy())

      print(
        '''
        1. Name
        2. Total Stat combination
        3. HP
        4. Attack
        5. Sp. attack
        '''
      )
      sortPick = input("what would u like to sort by")
      match sortPick:
        case "1":
          printCase3('Name')
        case "2":
          printCase3('Total')
        case "3":
          printCase3('HP')
        case "4":
          printCase3('Attack')
        case "5":
          printCase3('Sp. Atk')
    
    #4. Add data to favourites list
    case "4":
      nameOfMon = input('what is the name of the pokemon you wish to add to fave list')
      find_name_to_add = (next(item for item in convertToDict if item['Name'] == nameOfMon.title()))
      faveList.append(find_name_to_add)
      print(find_name_to_add)
    
    #5. Remove data from favourits list
    case "5":
      print('hello')


    #display favList
    case "6":
      print(faveList)








