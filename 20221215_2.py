"""
still not works
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

LINES = 4000000

for LINE in range(LINES*3//4, LINES):
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

    indexL = 0
    indexR = 0

    while indexL < len(ranges):
        while indexR < len(ranges):
            if indexL != indexR:
                Lleft = ranges[indexL][0]
                Lright = ranges[indexL][1]
                Rleft = ranges[indexR][0]
                Rright = ranges[indexR][1]
                if (Lright >= Rleft) and (Rright >= Lleft):
                    merged = [min(Lleft, Rleft), max(Lright, Rright)]
                    del ranges[max(indexL, indexR)]
                    del ranges[min(indexL, indexR)]
                    ranges.append(merged)
                    indexL = 0
                    indexR = -1
            indexR += 1
        indexL += 1
    if len(ranges) == 2:
        print(LINE, ranges)