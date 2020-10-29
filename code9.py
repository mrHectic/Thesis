def makeClock(goMain, j):
    try:
        cFile1 = open(goMain) 
        lines = cFile1.readlines()
        for i in lines:
            isClock = clockReg.findall(i) 
            if isClock:
                file = open(j + '_clock.txt', 'a+') 
                file.write(isClock[0] + '\n') 
                file.close()
            else:
                pass
    except FileNotFoundError:
        pass