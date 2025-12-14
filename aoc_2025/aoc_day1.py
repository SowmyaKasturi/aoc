# Implement a 10-minute tumbling window aggregator for a stream of log lines, where:
# Windows are fixed (00–10, 10–20, 20–30, …)
# Use event time, not processing time
# Late events up to 3 minutes are allowed (watermark = 3 minutes)
# Events later than the watermark must be dropped
# You must maintain:
# per-window user counts
# per-window valid / invalid / duplicate stats
# You must update only the current open window and any late but allowed windows
# You must process events as a generator, dedupe by request_id, and not use defaultdict.
# point = 50
# start = 0
# stop = 100
# csv="""L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

def read_file():
    with open("aoc_day1_part2.csv", "r") as fp:
        data = fp.read()
        for i in data.split("\n"):
            yield i

# password = 0
# _diff = 0
# lrotate = 0
# for i in read_file():
#     i.strip()
#     if i.startswith("L"):
#         rotate = int(i.split("L")[1])
#         _diff = (point - rotate)
#         point = (_diff) % stop
#     elif i.startswith("R"):
#         rotate = int(i.split("R")[1])
#         _diff = (point  + rotate)
#         point = _diff % stop
#     print(f"The dial is rotated{i} to point at {point}")
#     if point == 0:
#         password += 1
#     elif (point + rotate) > 100 :
#         password += ((point + rotate) // stop)
# print(password)
def count_zero_crossings(start, steps, direction):
    """
    Count how many times a rotation passes position 0,
    not including the final position.
    """
    if direction == "R":   # increasing direction
        return (start + steps) // 100

    else:  # L (decreasing direction)
        # Equivalent to starting at 'start' and moving backward
        # Pass 0 when cumulative backward distance exceeds start
        return (steps - start + 99) // 100


def compute_password(filename):
    point = 50   # initial position
    password = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            steps = int(line[1:])
            start = point

            # Count zero crossings during movement
            crossings = count_zero_crossings(start, steps, direction)

            # Move dial
            if direction == "R":
                point = (start + steps) % 100
            else:
                point = (start - steps) % 100

            # Count final position if it is 0
            if point == 0:
                crossings += 1

            password += crossings

    return password


# Example usage:
print(compute_password("aoc_day1_part2.csv"))

def part2(start: int = 50, dial_nums: int = 100) -> int:
    """
    Count how many times the dial passes through position 0 during rotations.
   
    Args:
        data: List of rotation instructions (e.g., ['L68', 'R48', ...])
        start: Starting position of the dial (default: 50)
        dial_nums: Number of positions on the dial (default: 100)
    
    Returns:
        Total number of times the dial points at 0 during all rotations
    """
    zero_counter = 0
    curr_pos = start
    data = read_file()
    for instruction in data:
        direction = instruction[0]
        clicks = int(instruction[1:])
        
        for _ in range(clicks): # simulate EVERY click
            if direction == "R":
                curr_pos = (curr_pos + 1) % dial_nums
            else:  # direction == "L"
                curr_pos = (curr_pos - 1) % dial_nums
            
            if curr_pos == 0:
                zero_counter += 1

    return zero_counter
print(part2())