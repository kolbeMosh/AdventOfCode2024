def main(data: list, n: int):
    stones = {}
    for entry in data:
        stones[entry] = stones.get(entry, 0) + 1
    
    cache = {}

    for i in range(n):
        stones = blink(stones, cache)
    total = sum(stones.values())
    return total

def blink(data: dict, cache: dict) -> dict:
    newData = {}
    
    for stone, count in data.items():
        if stone in cache:
            if type(cache[stone]) == list:
                for item in cache[stone]:
                    newData[item] = newData.get(item, 0) + count
            else:
                newData[cache[stone]] = newData.get(cache[stone], 0) + count
        else:
            if stone == 0:
                cache[stone] = 1
                newData[1] = newData.get(1, 0) + count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                part1 = int(str(stone)[:mid])
                part2 = int(str(stone)[mid:])
                cache[stone] = [part1, part2]
                newData[part1] = newData.get(part1, 0) + count
                newData[part2] = newData.get(part2, 0) + count
            else:
                transformed = stone * 2024
                cache[stone] = transformed
                newData[transformed] = newData.get(transformed, 0) + count
    return newData

result = main([0, 7, 198844, 5687836, 58, 2478, 25475, 894], 75)
print(result)