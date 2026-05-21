import re
test = ("find the error in the log path")
pattern = r'error'
if re.search(pattern,test):
    print("error found")
