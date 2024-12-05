data = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        data.append(line)


def check(row:int, col: int, data: list):
    horz = bhorz = vert = bvert = rdiag = brdiag = ldiag = bldiag = False
       
    canVert = len(data[row]) > row + 3
    canHorz = len(data[row]) > col + 3
    canbHorz = col-3 >= 0
    canbVert = row-3 >= 0
   
    if canHorz:
        horz = (data[row][col+1] + data[row][col+2] + data[row][col+3]) == "MAS"
   
    if canbHorz:
        bhorz = (data[row][col-1] + data[row][col-2] + data[row][col-3]) == "MAS"
       
    if canVert:
        vert = (data[row+1][col] + data[row+2][col]+ data[row+3][col]) == "MAS"
       
    if canbVert:
        bvert = (data[row-1][col] + data[row-2][col] + data[row-3][col]) == "MAS"
       
    if canHorz and canVert:
        rdiag = data[row+1][col+1] + data[row+2][col+2] + data[row+3][col+3] == "MAS"
       
    if canbHorz and canbVert:
        brdiag = (data[row-1][col-1] + data[row-2][col-2] + data[row-3][col-3]) == "MAS"
   
    if canVert and canbHorz:
        ldiag = (data[row+1][col-1] + data[row+2][col-2] + data[row+3][col-3]) == "MAS"
   
    if canbVert and canHorz:
        bldiag = data[row-1][col+1] + data[row-2][col+2] + data[row-3][col+3] == "MAS"
       
    return int(horz) + int(bhorz) + int(vert) + int(bvert) + int(rdiag) + int(brdiag) + int(ldiag) + int(bldiag)
   
occurs = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            occurs += check(i, j, data)
           
print(occurs)

