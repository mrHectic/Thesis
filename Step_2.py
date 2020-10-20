# begin importing of standard modules
import re
import random
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pprint as pp
import sys
# end importing of standard modules

# begin setting of home path variable and adding data directory to path import list
if 'Step_1.ipynb' or 'Step_1.py' or 'Step_1.exe' in os.listdir():
    home = os.getcwd()     
sys.path.append(os.path.join(home, 'data')) #This will add the data folder to the path variable so modules can be imported 
# end setting of home path variable and adding data directory to path import list

# begin creation Regular Expression that will check that a folder has been sanitized
validHash = re.compile(r'#\d{0,3}')
# end creation Regular Expression that will check that a folder has been sanitized

# begin import of created modules
try:   
    import ds
    import mypath
    input('''Success!!!

data.csv in the data directory now contains the path to all the Core folders of students.

Press any key to exit...''')
except ModuleNotFoundError:
    input('''Before Step_2 can be run, Step_1 must be run to success first.
This will ensure that the needed python modules are created in the data directory!

Please run Step_1 till a success message is displayed, and then Step_2 again

Press any key to exit...''')
# begin import of created modules

# begin recursive function defintion to find the Core path
def findDrivers2(filepath):
#     import ipdb; ipdb.set_trace()
    for i in os.listdir(filepath):
        newPath = os.path.join(filepath , i)
        if i in ['.git','.settings','Driver','Debug','.metadata']:
            pass
        elif i == 'Core':
            df.loc[df['hsh'] == validHash.findall(newPath)[0], ['CorePath']] = newPath
        elif os.path.isdir(newPath) == False:
            pass
        elif os.path.isdir(newPath) and i != 'Core':                   
            findDrivers2(newPath)
# end recursive function defintion to find the Core path

# begin importing and creation of a data frame
os.chdir(mypath.data)
df = pd.read_csv('data.csv')
# end importing and creation of a data frame

# begin creation of the drivers path column in dataDrame
df['CorePath'] = 'Invalid Repository'
# end creation of the drivers path column in dataDrame

# begin going into each repo and identify the path to the Core folder per student
os.chdir(mypath.repos)
filepath = mypath.repos
findDrivers2(filepath) #This is the recursive function that does the work
# end going into each repo and identify the path to the Core folder per student

# begin setting the dataframe to display well
pd.set_option('max_colwidth', 200)
df.drop(columns ='Unnamed: 0')
# end setting the dataframe to display well

# begin saving the dataframe into the csv file again
os.chdir(mypath.data)
df.to_csv('data.csv')
# end saving the dataframe into the csv file again

