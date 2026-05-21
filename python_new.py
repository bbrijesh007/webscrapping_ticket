import re
test = ("find the error in the log path")
pattern = r'error'
result = re.search(pattern,test)
print(result)

