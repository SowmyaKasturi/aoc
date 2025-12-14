from aoc_utils.file_operations import read_file
from collections import deque
data = {}
for i in read_file("aoc_day11.csv"):
    key, values = i.split(":")
    data.setdefault(key, [])
    data[key] = [str(i) for i in values.strip().split(" ")]
def dfs(node, path):
    if node in path:
        return 0

    new_path = path + [node]

    if node == "out":
        return int("fft" in new_path and "dac" in new_path)

    return sum(dfs(nd, new_path) for nd in data.get(node, []))

# for i in result:
#     print(i)

print(dfs("svr", []))