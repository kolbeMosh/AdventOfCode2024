'''
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number 
of times that number appears in the right list.
'''

def main() -> int:
    lst1 = []
    lst2 = []
    appearances = dict()
    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip()
            data = line.split("   ")

            lst1.append(int(data[0]))
            lst2.append(int(data[1]))
    
    for num in lst2:
        if num not in appearances:
            appearances[num] = 1
        else:
            appearances[num] = appearances[num] + 1
    
    similarityScore = 0
    for i in range(len(lst1)):
        similarityScore += findSimilarity(lst1[i], appearances)
    
    return similarityScore
        



def findSimilarity(a: int, appears: dict) -> int:
    if a in appears:
        return a*appears[a]
    return 0


print(main())