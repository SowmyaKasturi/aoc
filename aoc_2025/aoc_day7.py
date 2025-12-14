from collections import deque
from aoc_utils.file_operations import read_file

matrix = [[_ for _ in ",".join(i).split(",")] for i in read_file("aoc_day7.csv")]

rows = len(matrix)
cols = len(matrix[0])

queue = deque()
visited = set()
count = 0

# Locate S
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "S":
            queue.append((r+1, c))
            visited.add((r+1, c))
            break
splitters_hit = set()



while queue:
    row, col = queue.popleft()

    # Move downward until grid edge or splitter
    while 0 <= col < cols and row < rows and matrix[row][col] != "^":
        row += 1

    # Beam exits the grid
    if row >= rows or col < 0 or col >= cols:
        continue

    # Beam hits splitter
    if matrix[row][col] == "^":
        if (row, col) not in splitters_hit:
            splitters_hit.add((row, col))
            count += 1
        # Spawn left/right beams
        for nr, nc in [(row+1, col-1), (row+1, col+1)]:
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

print(count)
