"""
first part(star) only
"""
data = []
with open('15.in') as file:
    for line in file.readlines():
        line = line.strip().split(':')
        lhs_x = int(line[0].split()[2].split('=')[1][:-1])
        lhs_y = int(line[0].split()[3].split('=')[1])
        rhs_x = int(line[1].split()[4].split('=')[1][:-1])
        rhs_y = int(line[1].split()[5].split('=')[1])
        distance = abs(lhs_x - rhs_x) + abs(lhs_y - rhs_y)
        left = lhs_x - distance
        right = lhs_x + distance
        top = lhs_y - distance
        bottom = lhs_y + distance
        data.append([[left, top], [right, bottom]])

LINE = 2000000

ranges = []
for sensor in data:
    top = sensor[0][1]
    bottom = sensor[1][1]
    left = sensor[0][0]
    right = sensor[1][0]
    if LINE >= top and LINE <= bottom:
        y = (top + bottom) // 2
        dy = abs(LINE - y)
        ranges.append([left + dy, right - dy])
        print(ranges[-1])

low = min([item[0] for item in ranges])
high = max([item[1] for item in ranges])
print('PART 1 SOLUTION: ', high - low)
