import json
import pandas as pd 
import numpy as np

pd.set_option('display.max_rows', None)

cols = [0,1,2,4,3,5,6,8,10]
df = pd.read_excel("pokemonData.xlsx", usecols=cols)
convertToDict = (df.to_dict('records'))


#loading info from .txt file
def loadFaves():
  file = open("user_list.txt", "r")
  data = json.load(file)
  file.close()
  return data

#save contacts
def saveFaves(fileToSave):
  file = open("user_list.txt", "w")
  json.dump(fileToSave, file)
  file.close()


faveList = loadFaves()

def selectionSort(anArray, whatToSearch):
  for fill_slot in range(len(anArray)):
      min_position = fill_slot

      for post_fill in range(fill_slot +1, len(anArray)):
          
          if anArray[post_fill][whatToSearch] < anArray[min_position][whatToSearch]:
              min_position = post_fill

      anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]

#search for name functon
def searchName(list, name, inItem):
  for item in list:
      if item[inItem] == name:
          return list.index(item)

  return -1

def printCase3(searchBy):
  selectionSort(copy_to_disp, searchBy)
  for item in range(len(copy_to_disp)):
    print(copy_to_disp[item])

def user_account():
  loop_creds = True
  while loop_creds:
    print('''
    1. sign up
    2. login 
    ''')

    accauntPick = input("input the number of the option you want (1 or 2)")

    #sign up
    if accauntPick == "1":
      #ask user for username and password
      username = input("what would you like as a username")
      password = input("what would you like as a password")

      #check if the username already exists in the user_list.txt file
      loof_for_username_sign_up= searchName(faveList, username, 'username')

      if loof_for_username_sign_up == -1:
        dict = {
          "username": username,
          "password": password,
          "faves": []
        }
        faveList.append(dict)
        loop_creds = False
        return dict
      else:
        print('username is already in use, please pick a new one')

    #login
    elif accauntPick == "2":
      username = input('what is your username')
      password = input('what is your password')

      for i in range(len(faveList)):
        if faveList[i]['username'] == username and faveList[i]['password'] == password:
          print('login complete')

          dict = {
            "username": username,
            "password": password,
            'faves': []
          }
          return dict
          loop_creds = False
      else:
        print('incorrect username or password, try again')
    
    else:
      print('enter a correct number (1 or 2)')

user_info = user_account()
index_of_user = searchName(faveList, user_info['username'], 'username')

def print_fave():
  for i in range(len(faveList[index_of_user]['faves'])):
    print(faveList[index_of_user]['faves'][i])

def condSearch(poketype):
  filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
  print(df.loc[filt].to_string(index=False))

loop_main = True
while loop_main:
  print(
    '''
    1. Display all data
    2. Search for spacific data
    3. Sort the data 
    4. Add data to favourites list
    5. Remove data from favourits list
    6. Display favourites list
    7. Save Data
    8. Exit 
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
      inputMon = input('what type is the pokemon you like to display?').title()
      condSearch(inputMon)

    #3. Sort the data 
    case "3":

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
      find_name = searchName(convertToDict.copy(), nameOfMon, 'Name')

      #if statments for if found or not found
      if find_name == -1:
        print("pokemon doesnt exist")
      else:
        for d in faveList:
          if d['username']  == user_info['username'] and d['password']  == user_info['password']:
            d['faves'].append(convertToDict[find_name])
      print_fave()
    
    #5. Remove data from favourits list
    case "5":
      input_for_del = input("what is the name of the pokemon you wish to remove").title()

      for d in faveList:
        if d['username'] == user_info['username'] and d['password'] == user_info['password']:
          for i, faves in enumerate(d['faves']):
            if input_for_del in faves.values():
              d['faves'].pop(i)
      print_fave()

    #display favList
    case "6":
      print_fave()

    #save data
    case "7":
      saveFaves(faveList)   

    #exit program
    case "8":
      print("program end")
      loop_main = False