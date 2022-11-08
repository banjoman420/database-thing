import os 
import sys 
import pandas as pd 
import openpyxl
import xlrd
import json
import csv
loop = True

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









