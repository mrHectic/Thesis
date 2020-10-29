def makePins(goMain, j):   
    dfPins = pd.DataFrame(columns = ['Port', 'Pin', 'Mode','Pull-Type','Speed']) 
    try:
        cFileT = open(goMain) 
        lines = cFileT.readlines() 
    except FileNotFoundError:
        dfPins.to_csv(j + '_main.c.csv', index = False)
        lines = 'Empty repo'
        dfPins.loc[1] = lines   
    pinList = []
    validList = []
    modeList = []
    pullList = []
    speedList = []
    x = 0
    for i in lines:
        isValid = pinRegex1.findall(i)
        isPinLine = pinRegex2.findall(i)
        isModeLine = modeRegex.findall(i)
        isPullLine = pullRegex.findall(i)
        isSpeedLine = speedRegex.findall(i)
        isGpioInitLine = gpioInitRegex.findall(i)
        if isPinLine and isValid:
            pinList.extend(isPinLine[2:])
            validList.extend(isValid)      
        elif isModeLine:
            modeList.extend(isModeLine)
        elif isPullLine:
            pullList.extend(isPullLine)
        elif isSpeedLine:
            speedList.extend(isSpeedLine)
        elif isGpioInitLine and pinList and validList:
            dfTempPin = pd.DataFrame(columns = ['Port', 'Pin', 'Mode','Pull-Type','Speed']) 
            for i in pinList:
                dfPins.loc[x] = [isGpioInitLine[0]] +  [i] + [modeList] + [pullList] + [speedList]
                x += 1           
            pinList = []
            modeList = []
            pullList = []
            speedList = []
            validList = []
        else:
            pass
    os.chdir(mypath.data)
    dfPins.to_csv(j + '_pinout_main.c.csv', index = False)