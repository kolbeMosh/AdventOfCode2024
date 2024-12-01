'''
Maybe the lists are only off by a small amount! To find out, pair up the numbers
and measure how far apart they are. Pair up the smallest number in the left list 
Maybe the lists are only off by a small amount! To find out, pair up the numbers 
and measure how far apart they are. Pair up the smallest number in the left list 
with the smallest number in the right list, then the second-smallest left number 
with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to 
add up all of those distances. For example, if you pair up a 3 from the left list 
with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, 
the distance apart is 6.with the smallest number in the right list, then the 
second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add 
up all of those distances. For example, if you pair up a 3 from the left list with 
a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the 
distance apart is 6.

'''

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