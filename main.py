import json
import pandas as pd 
import numpy as np
loop = True

pd.set_option('display.max_rows', None)

cols = [0,1,2,4,3,5,6,8,10]
df = pd.read_excel("pokemonData.xlsx", usecols=cols)
convertToDict = (df.to_dict('records'))


#loading info from .txt file
def loadFaveList():
  file = open("FaveList.txt", "r")
  data = json.load(file)
  file.close()
  return data

#save contacts
def saveFaveList(fileToSave):
  file = open("FaveList.txt", "w")
  json.dump(fileToSave, file)
  file.close()

faveList = loadFaveList()

def selectionSort(anArray, whatToSearch):
  for fill_slot in range(len(anArray)):
      min_position = fill_slot

      for post_fill in range(fill_slot +1, len(anArray)):
          
          if anArray[post_fill][whatToSearch] < anArray[min_position][whatToSearch]:
              min_position = post_fill

      anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]

#search for name functon
def searchName(list, name,):
  for item in list:
      if item["Name"] == name:
          return list.index(item)

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

def userSignUp():
  username = input("what would you like as a username")
  password = input("what would you like as a password")

  dict = {
    "username": username,
    "password": password,
    "faves": []
  }
  return dict
  
user_info = userSignUp()
faveList.append(user_info)
print(faveList)

  
while loop:
  print(
    '''
    1. Display all data
    2. Search for spacific data
    3. Sort the data 
    4. Add data to favourites list
    5. Remove data from favourits list
    6. Display favourites list
    7. Save Data
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
      
      #case statments for sorting information 
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
      nameOfMon = input('what is the name of the pokemon you wish to add to fave list').title()
      find_name = searchName(convertToDict, nameOfMon)

      #if statments for if found or not found
      if searchName == -1:
        print("pokemon doesnt exist")
      else:
        for i in range(len(faveList)):
          if faveList[i]['username'] == user_info["username"] and faveList[i]['password'] == user_info['password']:
            faveList.append(convertToDict[find_name])
            print(i)







        # faveList.append(convertToDict[find_name])
        # print(convertToDict[find_name])
    
    #5. Remove data from favourits list
    case "5":
      input_for_del = input("what is the name of the pokemon you wish to remove").title()

      #search for name in list of dicts
      search_for_del = searchName(faveList, input_for_del)

      #if name is not found 
      if search_for_del == -1:
        print("pokemon doesnt exiat in list")

      #if name is found 
      else:
        faveList.pop(search_for_del)
        printFor()

    #display favList
    case "6":
      printFor()

    #save data
    case "7":
      saveFaveList(faveList)