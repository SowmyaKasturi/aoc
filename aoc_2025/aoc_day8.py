from aoc_utils.file_operations import read_file
matrix = [tuple(_ for _ in i.split(",")) for i in read_file("aoc_day8.csv")]
# sample ="""162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""
# output=40
result = 0
log = {}
def get_distance(row, next_row):
    x1,y1, z1 = (int(_) for _ in row)
    x2, y2, z2 = ( int(_) for _ in next_row)
    return pow(((x1-x2)**2 +  (y1-y2) ** 2 + (z1-z2) ** 2), 0.5)

pairs = {}
for row in range(0,len(matrix)-1):
    min_val = float('inf')
    for j in range(row+1, len(matrix)):
        pairs[(matrix[row], matrix[j]) ] = get_distance(matrix[row],matrix[j])

data = sorted(pairs.items(), key= lambda x:x[1])

connection  = []
count = 0

def find_circuits(node):
     for p in connection:
          if node in p:
               return p
final_pair = None
merged = set()
for _, v in data:
    a, b =_
    ca = find_circuits(a)
    cb = find_circuits(b)
    if ca is None and cb is None:
            connection.append({a,b})
    elif ca is not None and cb is None:
            ca.add(b)
    elif ca is None and cb is not None:
            cb.add(a)
    elif ca is not cb:
            connection.remove(ca)
            connection.remove(cb)
            merged = ca | cb
            connection.append(merged)
    # part 2
    if len(merged) == len(matrix):
          final_pair = (a,b)
          break
    # count += 1
    # if count == 1000:
    #       break
print(int(final_pair[0][0]) * int(final_pair[1][0]))
# result = 1
# for i in sorted(connection, key=lambda x:len(x), reverse=True)[:3]:
#       result *= len(i)
