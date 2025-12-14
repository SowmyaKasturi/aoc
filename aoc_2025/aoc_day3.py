from itertools import combinations
from aoc_utils.file_operations import read_file
"""
sample =987654321111111
811111111111119
234234234234278
818181911112111
output=357
"""
def max_subsequence(s):
    stack = []
    k = 12
    drop = len(s) - k
    for ch in s:
        int(ch)
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return int("".join(stack[:12]))
def get_maxjoltage():
    result = 0
    # i="811111111111119"
    for i in read_file("aoc_day3.csv"):
#     sample="""987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""
    # for i in sample.split("\n"):
        if i:
            
            # max_num = 0
            # for i in ("".join(i) for i in combinations(i,12)):
            #     max_num = max(max_num, int(i))
            # k = 0
            # l = []
            # while k < len(i)-12:
            #     l.append(int(i[k:k+12]))
            #     k += 1
            # print(max(l))
            result += max_subsequence(i)
    return result

print(get_maxjoltage())