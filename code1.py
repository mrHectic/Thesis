if 'Step_1.ipynb' or 'Step_1.py' or 'Step_1.exe' in os.listdir():
    home = os.getcwd()     
sys.path.append(os.path.join(home, 'data')) 

try:
    os.chdir('data')
    import mypath
except FileNotFoundError:
    pass
except ModuleNotFoundError:
    pass

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
    pass