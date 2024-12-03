'''
The unusual data (your puzzle input) consists of many reports, 
one report per line. Each report is a list of numbers called levels 
that are separated by spaces

The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are 
either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three
'''


def main():
    reports = []
    
    with open("d2Input.txt", 'r') as input:
        for line in input:
            line = line.strip()
            data = list(map(int, line.split(" ")))
            reports.append(data)

    print("Problem 1 Answer:")
    print(problem1(reports))
    print("Problem 2 Asnwer:")
    print(problem2(reports))

# Problem 1: 

def problem1(reports: list) -> int:
    safeReports = 0
    for report in reports:
        isSafe = checkSafe(report)
        if isSafe:
            safeReports += 1
    return safeReports

def checkSafe(arr: list) -> bool:
    increasing = True
    decreasing = True

    for i in range(len(arr)-1):
        diff = abs(arr[i+1] - arr[i])
        if diff < 1 or diff > 3:
            return False
        
        if arr[i] > arr[i+1]:
            increasing = False

        if arr[i] < arr[i+1]:
            decreasing = False

    return increasing or decreasing

# Problem 2:

def problem2(reports: list) -> int:
    safeReports = 0
    for report in reports:
        isSafe = checkSafe(report) or checkSafeRemoval(report)
        if isSafe:
            safeReports += 1
    return safeReports

def checkSafeRemoval(arr: list) -> bool:
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        if checkSafe(new_arr):
            return True
    return False

    
main()