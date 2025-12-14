# sample="""
# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """
# output=3
from aoc_utils.file_operations import read_file
def get_data():
    ranges = []
    ingredients = set()
    range_start_end = []
    def get_fresh_ingredients():
        count = 0
        for i in ingredients:
            for j in ranges:
                if i in j:
                    count += 1
                    break
        return count
    
    def get_all_fresh_ingredients():
        from operator import itemgetter
        range_list = sorted(range_start_end ,key=itemgetter(1))
        start, end = range_list[0][0], range_list[0][1]
        new_range_start_end = set()
        for rng in range(1,len(range_list)):
                print(rng, range_list[rng])
                if start in range(range_list[rng][0],range_list[rng][1] + 1 ) or\
                end in range(range_list[rng][0],range_list[rng][1] + 1):
                    start , end = min(start,  range_list[rng][0]), max(end, range_list[rng][1])
                else:
                    new_range_start_end.add((start, end))
                    start, end = range_list[rng][0],range_list[rng][1]
        new_range_start_end.add((start, end))
        return sum(len(range(i[0], i[1]+1)) for i in list(new_range_start_end))
               
    
    for i in read_file("aoc_day5.csv"):
        if i.strip():
            if "-" in i:
                start, end = (int(_) for _ in i.split("-"))
                ranges.append(range(start,end+1))
                range_start_end.append((start,end))
            else:
                ingredients.add(int(i))
    return get_fresh_ingredients(), get_all_fresh_ingredients()
print(get_data())