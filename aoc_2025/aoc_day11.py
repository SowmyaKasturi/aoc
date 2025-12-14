from aoc_utils.file_operations import read_file
from collections import deque
data = {}
for i in read_file("aoc_day11.csv"):
    key, values = i.split(":")
    data.setdefault(key, [])
    data[key] = [str(i) for i in values.strip().split(" ")]
queue = deque()
queue.append("you")
count = 0
while queue:
    _data = queue.popleft()
    if data[_data] and data[_data][0] == "out":
        count += 1
        continue
    for i in data[_data]:
        print(i)
        queue.append(i)
print(count)
