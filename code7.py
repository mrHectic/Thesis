iocRep = re.compile(r"\w*\.ioc")
pinRegRename = re.compile(r"(\w+)\.(GPIO_Label)=(\w+\s*\w+)")
clockReg = re.compile(r'RCC_OscInitStruct.\w*.*\w*\s*=\s*\w*')
pinRegex1 = re.compile(r'GPIO_InitStruct.Pin\s*=\s*')
pinRegex2 = re.compile(r'(\w+)')
modeRegex = re.compile(r'''
            GPIO_MODE_                  #This will match the first part
            (
            INPUT|
            OUTPUT_PP|
            OUTPUT_OD|
            AF_PP|
            AF_OD|
            ANALOG|
            IT_RISING|
            IT_FALLING|
            IT_RISING_FALLING|
            EVT_RISING|
            EVT_FALLING|
            EVT_RISING_FALLING)    
            ''', re.VERBOSE)
pullRegex = re.compile(r'''
            GPIO_NOPULL|
            GPIO_PULLUP|
            GPIO_PULLDOWN
            ''', re.VERBOSE)
speedRegex = re.compile(r'''
             GPIO_SPEED_FREQ_LOW|
             GPIO_SPEED_FREQ_MEDIUM|
             GPIO_SPEED_FREQ_HIGH|
             GPIO_SPEED_FREQ_VERY_HIGH
             ''', re.VERBOSE)
gpioInitRegex = re.compile(r'''
                 HAL_GPIO_Init\((\w+),
                 ''', re.VERBOSE)