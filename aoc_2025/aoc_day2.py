from aoc_utils.file_operations import read_file



def part1(file_content):
    result = 0
    file_content = read_file("aoc_day2.csv")
    for line in file_content:
        ranges = line.split(",")
        for range_str in ranges:
            if range_str:
                start, end = [int(_) for _ in range_str.split("-")]
                for number in range(start, end+1):
                    inp = str(number)
                    if len(inp) % 2 == 0:
                        half = (len(inp) // 2)
                        i = 0
                        while i < half and half < len(inp):
                            if inp[i] != inp[half]:
                                break
                            i += 1
                            half += 1
                        if half == len(inp):
                            result += int(inp)
    return result

def isinvalid(number):
    n = len(number)
    for k in range(1, n//2+1):
        if n % k != 0:
            continue
        pattern = number[:k]
        if pattern * (n//k) == number:
            return True
    return False
def part2():
    result = 0
    file_content = read_file("aoc_day2.csv")
    for line in file_content:
        ranges = line.split(",")
        for range_str in ranges:
            if range_str:
                start, end = [int(_) for _ in range_str.split("-")]
                for number in range(start, end+1):
                    if isinvalid(str(number)):
                        result += number
    return result


# print(f"Part1: {part1()}")
print(f"Part2: {part2()}")