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

#search for name functon
def searchName(list, name):
  for item in list:
      if item["Name"] == name:
          return faveList.index(item)

  return -1

#print for loop with key values
def printWithKey(inputUser):
  for key, value in faveList[inputUser].items():
      print(key, ":", value)

def printFor():
  for item in range(0, len(faveList)):
      print(faveList[item])

def printCase3(searchBy):
  selectionSort(copy_to_disp, searchBy)
  for item in range(len(copy_to_disp)):
    print(copy_to_disp[item])

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
      printFor()
    
    #5. Remove data from favourits list
    case "5":
      input_for_del = input("what is the name of the pokemon you wish to remove").title()

      search_for_del = searchName(faveList, input_for_del)

      if search_for_del == -1:
        print("pokemon doesnt exiat in list")
      else:
        faveList.pop(search_for_del)
        printFor()


    #display favList
    case "6":
      printFor()








