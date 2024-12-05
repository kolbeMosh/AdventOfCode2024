import re

def main() -> int:
    text = ""
    with open("input.txt", "r") as file:
        for line in file:
            text += line

def getSumMul(txt: str) -> list:
    regex = re.compile('mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)')
    numPattern = re.compile('[0-9]+')
    tokens = regex.findall(txt)

    summation = 0
    do = True
    for token in tokens:
        if token == 'don\'t()':
            do = False
        elif token == 'do()':
            do = True
        elif do:
            data = numPattern.findall(token)
            summation += int(data[0]) * int(data[1])
            
    return summation

print(getSumMul(text))