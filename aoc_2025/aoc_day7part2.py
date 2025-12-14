from aoc_utils.file_operations import read_file

matrix = [[_ for _ in ",".join(i).split(",")] for i in read_file("aoc_day7.csv")]

rows = len(matrix)
cols = len(matrix[0])

def find_path(row, col):
    if col < 0  or col >= cols:
        return 0
    if row == rows - 1:
        return 1
    cell = matrix[row][col]
    if cell == ".":
        return find_path(row + 1, col)
    if cell == "^":
        return find_path(row+1, col-1) + find_path(row+1, col + 1)

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "S":
            start_r = r + 1
            start_c = c
            # print(find_path(r+1,c))
            break

dp = [ [0]*cols for _ in range(rows) ]

# Bottom row: each reachable cell = 1 timeline
for c in range(cols):
    dp[rows-1][c] = 1

for r in range(rows-2, -1, -1):
    for c in range(cols):
        if matrix[r][c] in ".S":
            dp[r][c] = dp[r+1][c]
        elif matrix[r][c] == "^":
            left = dp[r+1][c-1] if c-1 >= 0 else 0
            right = dp[r+1][c+1] if c+1 < cols else 0
            dp[r][c] = left + right

answer = dp[start_r+1][start_c]
print(answer)
