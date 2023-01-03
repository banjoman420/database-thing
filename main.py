import json
import pandas as pd 
import numpy as np

#set get excel file, set display type, select cols to use, and convert the whole thing to a dictionary
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

# faveList = loadFaves()

#search for name functon
def searchName(list, name, inItem):
  for item in list:
      if item[inItem] == name:
          return list.index(item)

  return -1

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
      username, password = get_info()

      # check if the username already exists in the user_list.txt file
      look_for_username_sign_up= searchName(faveList, username, 'username')

      if look_for_username_sign_up == -1:
        info = signup_func(username, password, faveList)
        return info
        loop_creds = False
      else:
        print('username is already in use, please pick a new one')

    #login
    elif accauntPick == "2":
      #get username and password from user
      username, password = get_info()

      #run the login function that will check if the username and password exist in the big data and then return it
      info = login_func(username, password, faveList)

      print('login complete')
      return info
      loop_creds = False
    
    else:
      print('enter a correct number (1 or 2)')

def get_info():
  username = input('what is your username')
  password = input('what is your password')
  return username, password

def signup_func(username, password, list):
  dict = {
    "username": username,
    "password": password,
    "faves": []
  }
  list.append(dict)
  return dict

def login_func(username, password, list):
  for i in range(len(list)):
    if list[i]['username'] == username and list[i]['password'] == password:
      dict = {
        "username": username,
        "password": password
      }
      return dict

#get index of user to be able to use in other functions 
def look_index():
  #get index of username since its unique
  check_user = searchName(faveList, user_info['username'], 'username')
  #check if that username has the password that the user inputed
  if faveList[check_user]['password'] == user_info['password']:
    return check_user

#print faveList
def print_fave():
  for i in range(len(faveList[index_of_user]['faves'])):
    print(faveList[index_of_user]['faves'][i])

#search using pandas
def condSearch(poketype):
  filt = (df['Type 1'] == poketype) | (df["Type 2"] == poketype)
  print(df.loc[filt].to_string(index=False))

def selectionSort(arr, key, ascending=True):
  #function to determain of acending or decending
  def comparator(x, y):
    return x < y if ascending else x > y

  for fill_slot in range(len(arr)):
    # Set minimum position to current fill_slot
    min_position = fill_slot
    # Loop through list start at the element after the current fill_slot
    for post_fill in range(fill_slot + 1, len(arr)):
      # If the element at post_fill is less than (or greater than if ascending is False) the element at min_position, set min_position to post_fill
      if comparator(arr[post_fill][key], arr[min_position][key]):
        min_position = post_fill
    # Swap the element at min_position with the element at fill_slot
    arr[min_position], arr[fill_slot] = arr[fill_slot], arr[min_position]

def printCase3(searchBy, yes_or_no):
  selectionSort(convertToDict, searchBy, yes_or_no)
  for item in range(len(convertToDict)):
    print(convertToDict[item])

def generate_sort_options():
  sort_keys = ['Name', 'Total', 'HP', 'Attack', 'Sp. Attack', 'Speed']
  options = []
  for key in sort_keys:
    options.append(f"{key} (ascending)")
    options.append(f"{key} (decending)")
  return options

def sortDicts():
  options = generate_sort_options()
  for i, option in enumerate(options):
    print(f"{i + 1}. {option}")

  sort_pick = input("What would you like to sort by? ")
  sort_pick = int(sort_pick) - 1
  sort_key = options[sort_pick].split()[0]
  ascending = options[sort_pick].endswith("(ascending)")
  printCase3(sort_key, ascending)

#remove info from 'faves' 
def remove_from_faves(input_for_del):
  for i, faves in enumerate(faveList[index_of_user]['faves']):
    if input_for_del in faves.values():
      faveList[index_of_user]['faves'].pop(i)
  else:
    print('Pokemon doesnt exist in list')

def add_data(does_exist, check_dub):
  #if statments for if found or not found
  if does_exist == -1:
    print("pokemon doesnt exist")
  elif check_dub != -1:
    print('pokemon already exists in favelist')
  else:
    #append info
    faveList[index_of_user]['faves'].append(convertToDict[does_exist])

def main():
  #main loop
  loop_main = True
  while loop_main:
    print(
      '''
      1. Display all data
      2. Filter for spacific type
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
        #use pandas to convert to string and print out (converted to string so the index can be set to false, this makes it so the index doesnt print out with the main information)
        print(df.to_string(index=False))
      
      #2. Filter for spacific type
      case "2":
        #gather user input
        inputMon = input('what type is the pokemon you like to display?').title()

        #set a condition to search by and search
        condSearch(inputMon)

      #3. Sort the data 
      case "3":
        #match statments that sort the data
        sortDicts()
      
      #4. Add data to favourites list
      case "4":
        #gain user input
        nameOfMon = input('what is the name of the pokemon you wish to add to fave list').title()

        #use the searchName() funtion to check if the user input exists in the dictionary and gather the index of the intended pokemon
        find_name = searchName(convertToDict, nameOfMon, 'Name')

        #checks for duplicate values in users faveList
        check_dupe = searchName(faveList[index_of_user]['faves'],nameOfMon,'Name')

        #use find_name and check_dupe to make sure the input is an actual pokemon and that it isnt a duplicate
        add_data(find_name, check_dupe)
      
      #5. Remove data from favourits list
      case "5":
        #user injput for what to remove
        input_for_del = input("what is the name of the pokemon you wish to remove").title()

        #call function that removes intended pokemon
        remove_from_faves(input_for_del)

      #display favList
      case "6":
        print_fave()

      #save data
      case "7":
        print('info saved')
        saveFaves(faveList)  
         
      #exit program
      case "8":
        print("PROGRAM END")
        loop_main = False

#*****calling everything for thing to start*****#

#load big list of data 
faveList = loadFaves()

#user login/signup 
user_info = user_account()

#get index of user to use for other functions
index_of_user = look_index()

#main function with all of the cases 
main()