from aoc_utils.file_operations import read_file
matrix = [[_ for _ in i] for i in read_file("aoc_day4.csv")]
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
row = len(matrix)
col = len(matrix[0])
def forklift():
    result = 0
    # smaple="""
    # ..@@.@@@@.
    # @@@.@.@.@@
    # @@@@@.@.@@
    # @.@@@@..@.
    # @@.@@@@.@@
    # .@@@@@@@.@
    # .@.@.@.@@@
    # @.@@@.@@@@
    # .@@@@@@@@.
    # @.@.@@@.@."""
    # # result=13
    # part 2 result is 43
    for i in range(0,row):
        for j in range(0, col):
            if matrix[i][j] == "@":
                count = 0
                for di, dj in directions:
                        ni, nj = i+di, j + dj
                        if  ni in range(row) and  nj in range(col) and matrix[ni][nj] == "@" :
                            count += 1
                if count < 4:
                    matrix[i][j] = "x"
                    result += 1
    return result

total_sum=0
while True:
    
    result = forklift()
    if result == 0:
        break
    total_sum += result
print(total_sum)


   