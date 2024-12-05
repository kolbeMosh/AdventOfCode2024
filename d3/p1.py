import re

text = ""
with open("input.txt", "r") as file:
    for line in file:
        text += line

def getSumMul(txt: str) -> list:
    regex = re.compile('mul\([0-9]*,[0-9]*\)')
    numPattern = re.compile('[0-9]+')
    tokens = regex.findall(txt)
    summation = 0
    for token in tokens:
        data = numPattern.findall(token)
        summation += int(data[0]) * int(data[1])
    return summation
    
print(getSumMul(text))