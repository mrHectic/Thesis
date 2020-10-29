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