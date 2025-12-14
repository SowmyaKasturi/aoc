from aoc_utils.file_operations import read_file
matrix = [[_ for _ in i.strip().split(",")] for i in read_file("aoc_day6.csv")]

def get_sum():
    result_sum = 0
    for col in range(len(matrix[0])):
        add_result = 0
        mul_result = 1
        for row in range(len(matrix)-1):
            if "+" in matrix[-1][col]:
                add_result += int(matrix[row][col])
            if "*" in matrix[-1][col]:

                mul_result *= int(matrix[row][col])
        result_sum = result_sum + add_result + (mul_result if mul_result > 1 else 0)
    return result_sum

print(get_sum())
