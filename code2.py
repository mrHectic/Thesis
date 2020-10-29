stdNumRegex = re.compile(r'_(\d{8}$)')
replaceList = re.compile(r"(\[')(\d{8})('\])")
rg = re.compile(r'\d{8}')
validHash = re.compile(r'#\d{0,3}$')