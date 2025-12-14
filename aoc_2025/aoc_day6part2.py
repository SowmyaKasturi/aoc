from aoc_utils.file_operations import read_file
matrix = []
"""sample=123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

output = 3263827"""
for i in read_file("aoc_day6part2.csv"):
    temp = []
    for ch in i:
        temp.append(ch)
    matrix.append(temp)

def get_sum():
    result_sum = 0
    add_result = 0
    mul_result = 1
    for col in range(len(matrix[0])):
        
        
        _col = "".join( matrix[row][col] for row in range(len(matrix))).strip()
        print(_col)
        if not _col:
            print(col, add_result, result_sum, mul_result)
            result_sum = result_sum + add_result + (mul_result if mul_result > 1 else 0)
            add_result = 0
            mul_result = 1
            
        else:
            if "+" in _col:
                op = "add"
                _col = _col[:-1]
            elif "*" in _col:
                op = "mul"
                _col = _col[:-1]
            if op == "add":
                add_result += int(_col)
            else:
                mul_result *= int(_col)
    result_sum = result_sum + add_result + (mul_result if mul_result > 1 else 0)    
    return result_sum

print(get_sum())
