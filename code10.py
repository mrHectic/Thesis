def searchIoc(lines, j):
    x = 0
    dfIoc = pd.DataFrame(columns = ['Pin', 'Label']) 
    for i in lines:
        list1 = pinRegRename.findall(i)
        if list1:
            tup1 = list1[0]
            dfIoc.loc[x] = [tup1[0]] + [tup1[2]]
            os.chdir(mypath.data)               
        x += 1
    dfIoc.to_csv(j + '_ioc.csv', index = False)