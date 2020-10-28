
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

# begin importing of path module
try:
    os.chdir('data')
#     yes = input('#3 \n') #This was used to debug code
    import mypath
except FileNotFoundError:
#     yes = input('#4 \n') #This was used to debug code
#     print('The data directory does not exist yet')
    pass
except ModuleNotFoundError:
#     yes = input('#5 \n') #This was used to debug code
#     print('The module mypath.py does not exist')
    pass
# end importing of path module

# begin creation of path module nad data directory
try:
    os.chdir(home)
    os.mkdir('data')
    os.chdir('data')
    fileObj = open('mypath.py', 'w')
    fileObj.write('home = ' + pp.pformat(home) + '\n')
    fileObj.write('repos = ' + pp.pformat(os.path.join(home, 'stdRepos')) + '\n')
    fileObj.write('data = ' + pp.pformat(os.path.join(home, 'data')) + '\n')
    fileObj.close()
    import mypath
except FileExistsError:
#     print('The data dir already exists and cannot be made')
    pass
# end creation of path module nad data directory

# begin switch path to home
os.chdir(mypath.home)
# end switch path to home

# begin regex initilization
stdNumRegex = re.compile(r'_(\d{8}$)')
replaceList = re.compile(r"(\[')(\d{8})('\])")
rg = re.compile(r'\d{8}')
validHash = re.compile(r'#\d{0,3}$')
# end regex initilization

# begin creation of stdRepos directory
if  'stdRepos' not in os.listdir():
    ans = input('''There is no directory named stdRepos! For the sanitation process to work 
the stdRepos folder must be in the same directory as Step_1 
Would you like to create this directory?
    
[y\\n]

''')
    
    if ans == 'y':
        os.mkdir('stdRepos')
        input('''
The stdRepos directory has been created! 
Please unzip all student repositories in the stdRepos directory and run Step_1 again!

Type any key to exit...

''')
        sys.exit()
    elif ans == 'n':
        sys.exit()
# end creation of stdRepos directory

# begin creation of list with all student numbers in path.repos folder
# if there is an invalid problem error 3.2 will display in terminal
os.chdir(mypath.repos)
newList = list(filter(rg.findall, os.listdir()))
os.chdir(mypath.home)
# end creation of list with all student numbers in path.repos folder

# begin checking that there is nothing else in the stdRepos directory but valid folders
os.chdir(mypath.repos)
invalidFiles = []
for i in os.listdir():
    if not stdNumRegex.search(i) and not validHash.search(i):
       invalidFiles.append(i)
    else:
        pass
  
if invalidFiles:
    print('The following are invalid files in the stdRepos directory: \n')
    for i in invalidFiles:
        print(i)
    input('\nDelete these files and try again \nType any key to exit... \n')
    sys.exit()
# end checking that there is nothing else in the stdRepos directory but valid folders

# begin the population of dict with student numbers and creation of the ds.py module
os.chdir(mypath.repos)
if newList: # This will check that there is actually something in the stdRepos file that is a student number
    
    dictStd = {} 
    listOfIndexes = []
    j = 0
    
    for i in os.listdir(): # This for loop creates a list of idexes equal to the number of student repositories
        listOfIndexes.append(j)
        j += 1

    random.shuffle(listOfIndexes) # This ensures that the indexes are randomly linked to student numbers
    j = 0
    
    for i in os.listdir(): # This for loop will assign a hash value to a student number key in the dictionary
        dictStd.setdefault(replaceList.sub(r'\2', str(stdNumRegex.findall(i))), '#' + str(listOfIndexes[j]))
        j += 1
    # This code will create the ds module
    os.chdir(mypath.data)
    fileObj = open('ds.py', 'w')
    fileObj.write('dictStd = ' + pp.pformat(dictStd) + '\n')
    fileObj.close()
    os.chdir(mypath.home)
# end the population of dict with student numbers and creation of the ds.py module

# begin creation of ds module containing all the student numbers 
try:
    os.chdir(mypath.data)
    import ds
#     yes = input('Student numbers detected and subsequent hash codes created and linked! \n') #This was used to debug code
    dictStd = ds.dictStd
except ModuleNotFoundError:
#     print('import ds did not work')
    yes = input('#Error 3.2: import ds did not work module not found \nMake sure there is a valid student repository in the stdRepos folder and that it is unzipped! \nThen run Step_1 again') #This was used to debug code
except FileNotFoundError:
#     print('data directory does not exist yet')
    yes = input('#Error 3.3: data directory does not exist yet\n') #This was used to debug code
# end creation of ds module containing all the student numbers 

# begin the creation of a data frame from the dictionery
try:
    df = pd.DataFrame(ds.dictStd.items())
    df.rename(columns={0: "std", 1: "hsh"}, inplace = True)
#     yes = input('dataframe was created\n') #This was used to debug code
except NameError:
#     yes = input('#Error 4.1: Name Error\n') #This was used to debug code
    pass
#end the creation of a data frame from the dictionery

# begin renaming of all folders to hash codes
os.chdir(mypath.repos)
for i in os.listdir():
    for x, row in df.iterrows():
        try:
            if df.iloc[x][0] in stdNumRegex.findall(i):
                os.rename(i, df.iloc[x][1])
            else:
                pass
        except FileExistsError:
            print("Already renamed")
        except NameError:
            print("The Data Frame has not been initilazed")
# end renaming of all folders to hash codes

# begin adding of columns to frame
df['Perfect Repository Upload'] = False
# end adding of columns to frame

# begin detection of perfect repos
for x , i in enumerate (os.listdir()):
    os.chdir(mypath.repos) #goes back to stdRepos 
    os.listdir(os.path.join(mypath.repos ,  str(i))) #This shows the content of each #number
    if os.listdir(os.path.join(mypath.repos ,  str(i))).count('Core' and 'Debug' and 'Drivers') == 1:
        df.loc[df['hsh'] == str(i), ['Perfect Repository Upload']] = True
# end detection of perfect repos

# begin storing data frame
os.chdir(mypath.data)
df.to_csv('data.csv', index = False)
input('''Success!!!
 
All the folders have been renamed according to hash codes and a csv has been created in the data directory

You can now run Step_2!!

Press any key to exit...''')
# end storing data frame

