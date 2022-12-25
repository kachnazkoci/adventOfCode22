"""
--- Day 22: Monkey Map ---
The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly
the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field,
you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles
(on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

A number indicates the number of tiles to move in the direction you are facing. If you run into a wall,
you stop moving forward and continue with the next instruction.
A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place;
it does not change your current tile.
So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right
(from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board.
In other words, if your next tile is off of the board, you should instead look
in the direction opposite of your current facing as far as you can until you find the opposite edge of the board,
then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B;
if you are at C and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.
It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall
in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit,
the full path taken by the above example looks like this:

        >>v#
        .#v.
        #.v.
        ..v.
...#...v..v#
>>>v...>#.>>
..#v...#....
...>>>>v..#.
        ...#....
        .....#..
        .#......
        ......#.
To finish providing the password to this strange input device,
you need to determine numbers for your final row, column, and facing as your final position appears
from the perspective of the original map. Rows start from 1 at the top and count downward; columns start
from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with
no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
The final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So,
the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?

Your puzzle answer was 164014.

--- Part Two ---
As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes.
Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map,
you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
You still start in the same position and with the same facing as before, but the wrapping rules are different.
Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map,
this can look a little strange. In the above example, if you are at A and move to the right,
you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.
Walls still block your path, even if they are on a different face of the cube. If you are at E facing up,
your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path
taken by the above example now looks like this:

        >>v#
        .#v.
        #.v.
        ..v.
...#..^...v#
.>>>>>^.#.>>
.^#....#....
.^........#.
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.
The final password is still calculated from your final position and facing from the perspective of the map.
In this example, the final row is 5, the final column is 7, and the final facing is 3,
so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.

Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?

Your puzzle answer was 47525.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '22.in'
data = open(infile).read()
lines = [x for x in data.split('\n')]

G, instr = data.split('\n\n')
G = G.split('\n')
instr = instr.strip()

D = [(-1,0),(0,1),(1,0),(0,-1)]

R = len(G)
C = len(G[0])
for r in range(R):
    while len(G[r]) < C:
        G[r] += ' '
    assert len(G[r])==C

CUBE = C//3
assert CUBE == R//4
#print(CUBE)

# .12
# .3.
# 54.
# 6..
REGION = [(0,1),(0,2),(1,1),(2,1),(2,0),(3,0)]

def regionToGlobal(r,c,region):
    rr,cc = REGION[region-1]
    return (rr*CUBE+r,cc*CUBE+c)

def getRegion(r,c):
    for i,(rr,cc) in enumerate(REGION):
        if rr*CUBE<=r<(rr+1)*CUBE and cc*CUBE<=c<(cc+1)*CUBE:
            return (i+1, r-rr*CUBE, c-cc*CUBE)
    assert False, (r,c)

def newCoords(r,c,d,nd):
    if d==0:
        assert r==0
        x = c
    if d==1:
        assert c==CUBE-1
        x = r
    if d==2:
        assert r==CUBE-1
        x = CUBE-1-c
    if d==3:
        assert c==0
        x = CUBE-1-r

    if nd==0:
        return (CUBE-1,x)
    if nd==1:
        return (x,0)
    if nd==2:
        return (0,CUBE-1-x)
    if nd==3:
        return (CUBE-1-x,CUBE-1)

#  3   6
# 542 512
#  6   3

#  1   5
# 532 164
#  4   2

#  3   3
# 124 154
#  6   6

def getDest(r,c,d,part):
    if part == 1:
        r = (r+D[d][0])%R
        c = (c+D[d][1])%C
        while G[r][c]==' ':
            r = (r+D[d][0])%R
            c =(c+D[d][1])%C
        return (r,c,d)

    region,rr,rc = getRegion(r,c)
    # 0=up, 1=right,2=down,3=left
    # If I am leaving region R in direction D, I enter region NR in direction ND
    newRegion,nd = {
        (4,0):(3,0), (4,1):(2,3), (4,2):(6,3), (4,3):(5,3),
        (1,0):(6,1), (1,1):(2,1), (1,2):(3,2), (1,3):(5,1),
        (3,0):(1,0), (3,1):(2,0), (3,2):(4,2), (3,3):(5,2),
        (6,0):(5,0), (6,1):(4,0), (6,2):(2,2), (6,3):(1,2),
        (2,0):(6,0), (2,1):(4,3), (2,2):(3,3), (2,3):(1,3),
        (5,0):(3,1), (5,1):(4,1), (5,2):(6,2), (5,3):(1,1)}[(region,d)]

    nr,nc = newCoords(rr,rc,d,nd)
    assert 0<=nr<CUBE and 0<=nc<CUBE
    nr,nc = regionToGlobal(nr,nc,newRegion)
    assert G[nr][nc] in ['.','#'], f'{G[nr][nc]}'
    return (nr,nc,nd)

def solve(part):
    # compute starting location
    r = 0
    c = 0
    d = 1
    while G[r][c] != '.':
        c += 1

    i = 0
    while i < len(instr):
        n = 0
        while i<len(instr) and instr[i].isdigit():
            n = n*10 + int(instr[i])
            i += 1
        for _ in range(n):
            #print(r,c,d)
            assert G[r][c]=='.',(r,c)
            rr = (r+D[d][0])%R
            cc = (c+D[d][1])%C
            if G[rr][cc]==' ':
                (nr,nc,nd) = getDest(r,c,d,part)
                #print(f'r={r} c={c} rr={rr} cc={cc} nr={nr} nc={nc} region={getRegion(r,c)} d={d} newRegion={getRegion(nr,nc)} nd={nd}')
                if G[nr][nc]=='#':
                    break
                (r,c,d) = (nr,nc,nd)
                continue
            elif G[rr][cc]=='#':
                break
            else:
                r = rr
                c = cc
        if i==len(instr):
            break
        turn = instr[i]
        if turn == 'L':
            d = (d+3)%4
        elif turn == 'R':
            d = (d+1)%4
        else:
            assert False, (i,instr[i:],instr[i])
        i += 1
        #print('TURN', d)
    DV = {0:3,1:0,2:1,3:2}
    return ((r+1)*1000 + (c+1)*4 + DV[d])
print(solve(1))
print(solve(2))