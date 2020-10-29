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

os.chdir(mypath.repos)
newList = list(filter(rg.findall, os.listdir()))
os.chdir(mypath.home)

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
