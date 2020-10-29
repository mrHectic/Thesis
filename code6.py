def findCore(filepath):
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
            findCore(newPath)

findCore(mypath.repos)
