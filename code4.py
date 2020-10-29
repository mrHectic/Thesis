if newList:
    dictStd = {} 
    listOfIndexes = []
    j = 0 
    for i in os.listdir(): 
        listOfIndexes.append(j)
        j += 1
    random.shuffle(listOfIndexes) 
    j = 0
    for i in os.listdir():
        dictStd.setdefault(replaceList.sub(r'\2', str(stdNumRegex.findall(i))), '#' + str(listOfIndexes[j]))
        j += 1
    os.chdir(mypath.data)
    fileObj = open('ds.py', 'w')
    fileObj.write('dictStd = ' + pp.pformat(dictStd) + '\n')
    fileObj.close()
    os.chdir(mypath.home)
try:
    os.chdir(mypath.data)
    import ds
    dictStd = ds.dictStd
except ModuleNotFoundError:
    pass
except FileNotFoundError:
    pass
