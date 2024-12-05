data = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        data.append(line)

def check(row: int, col: int, data) -> bool:
    if data[row][col] == "A":
        return False
       
    if col+2 < len(data) and row+2 < len(data):
        txt = data[row][col] + data[row+1][col+1] + data[row+2][col+2]
        txt2 = data[row][col+2] + data[row+1][col+1] + data[row+2][col]
        return (txt == "MAS" or txt == "SAM") and (txt2 == "MAS" or txt2 == "SAM")
    return False

occurs = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        occurs += int(check(i, j, data))
       
print(occurs)