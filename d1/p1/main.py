def main() -> int:
    lst1 = []
    lst2 = []
    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip()
            data = line.split("   ")
            lst1.append(int(data[0]))
            lst2.append(int(data[1]))
    
    lst1.sort()
    lst2.sort()

    totalDistance = 0
    for i in range(len(lst1)):
        totalDistance += findDistance(lst1[i], lst2[i])
    return totalDistance
    


def findDistance(a: list, b: list) -> int:
    return abs(a-b)


print(main())