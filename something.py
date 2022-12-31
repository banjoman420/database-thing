import pandas as pd

cols = [0,1,2,4,3,5,6,8,10]
df = pd.read_excel("pokemonData.xlsx", usecols=cols)
convertToDict = (df.to_dict('records'))



def selectionSort(arr, key, ascending=True):

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
    sort_keys = ['Name', 'Total', 'HP', 'Attack', 'Sp. Attack']
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

# def sortDicts():
#   print(
#     '''
#     1. Name (A-Z)
#     2. Name (Z-A)
#     3. Total stats (Lowest to Highest)
#     4. Total stats (Highest to Lowest)
#     5. HP (Lowest to Highest)
#     6. HP (Highest to Lowest)
#     7. Attack (Lowest to Highest)
#     8. Attack (Highest to Lowest)
#     9. Sp. Attack (Lowest to Highest)
#     10. Sp. Attack (Highest to Lowest)
#     '''
#   )

#   #case statments for sorting information 
#   sortPick = input("what would u like to sort by")
#   match sortPick:
#     case "1":
#       printCase3('Name', True)
#     case "2":
#       printCase3('Name', False)
#     case "3":
#       printCase3('Total', True)
#     case "4":
#       printCase3('Total', False)
#     case "5":
#       printCase3('HP', True)
#     case "6":
#       printCase3('HP', False)
#     case "7":
#       printCase3('Attack', True)
#     case "8":
#       printCase3('Attack', False)
#     case "9":
#       printCase3('Sp. Attack', True)
#     case "10":
#       printCase3('Sp. Attack', False)
sortDicts()