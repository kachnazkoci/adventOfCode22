"""
--- Day 16: Proboscidea Volcanium ---
The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

Your puzzle answer was 1923.

--- Part Two ---
You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only 26 minutes to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
With the elephant helping, after 26 minutes, the best you could do would release a total of 1707 pressure.

With you and an elephant working together for 26 minutes, what is the most pressure you could release?

Your puzzle answer was 2594.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
# PART 1
with open("16.in") as f:
    input = f.read()
    input = input.replace("Valve ", "")
    input = input.replace("has flow rate=", "")
    input = input.replace("; tunnels lead to valves", "")
    input = input.replace("; tunnel leads to valve", "")
    input = input.replace(", ", ",")
    lines = input.split("\n")

flows = {}
tunnels = {}
for line in lines:
    valve, flow_str, tunnels_str = line.split(" ")

    flows[valve] = int(flow_str)
    tunnels[valve] = tunnels_str.split(",")


class State:
    def __init__(self, valve, open_valves, time) -> None:
        open_valves_str = ";".join(open_valves)
        self.hash_str = f"{valve};{open_valves_str};{time}"

    def __hash__(self) -> int:
        return self.hash_str.__hash__()

    def __eq__(self, __o: object) -> bool:
        return self.hash_str == __o.hash_str


cache = {}


def dfs(current_valve, current_flow, open_valves, time):
    key = State(current_valve, open_valves, time)
    if key in cache:
        return cache[key]

    if time <= 0:
        return current_flow

    max_flow = 0

    if current_valve not in open_valves and flows[current_valve] > 0:
        next_open_valves = open_valves.copy()
        next_open_valves.append(current_valve)
        next_flow = current_flow + flows[current_valve] * (time - 1)
        max_flow = dfs(current_valve, next_flow, next_open_valves, time - 1)

    for tunnel in tunnels[current_valve]:
        max_flow = max(max_flow, dfs(tunnel, current_flow, open_valves.copy(), time - 1))

    cache[key] = max_flow
    return max_flow


print(dfs("AA", 0, [], 30))

# PART 2
with open("16.in") as f:
    input = f.read()
    input = input.replace("Valve ", "")
    input = input.replace("has flow rate=", "")
    input = input.replace("; tunnels lead to valves", "")
    input = input.replace("; tunnel leads to valve", "")
    input = input.replace(", ", ",")
    lines = input.split("\n")

valves = []
positive_valves = []
flows = {}
tunnels = {}

for line in lines:
    valve, flow_str, tunnels_str = line.split(" ")

    flows[valve] = int(flow_str)
    tunnels[valve] = tunnels_str.split(",")
    valves.append(valve)
    if flows[valve] > 0:
        positive_valves.append(valve)

distances = {valve_from: {valve_to: 0 if valve_from == valve_to else 99999 for valve_to in valves} for valve_from in
             valves}

for valve in valves:
    for tunnel in tunnels[valve]:
        distances[valve][tunnel] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])


def dfs(current_valve, open_valves, time):
    result = []
    result.append(open_valves)

    for next_valve in positive_valves:
        if next_valve not in open_valves and distances[current_valve][next_valve] < time:
            next_open_valves = open_valves.copy()
            next_open_valves.append(next_valve)
            next_result = dfs(next_valve, next_open_valves, time - distances[current_valve][next_valve] - 1)
            result.extend(next_result)

    return result


time = 26
start_valve = "AA"
paths = dfs(start_valve, [], time)
path_flows = [0 for _ in paths]

for i, path in enumerate(paths):
    flow = 0
    remaining_time = time
    current_valve = start_valve

    for next_valve in path:
        remaining_time -= (distances[current_valve][next_valve] + 1)
        flow += flows[next_valve] * remaining_time
        current_valve = next_valve

    path_flows[i] = flow

max_flow = 0
paths = list(map(set, paths))

for i in range(len(paths)):
    for j in range(i + 1, len(paths)):
        if paths[i].isdisjoint(paths[j]):
            max_flow = max(max_flow, path_flows[i] + path_flows[j])

print(max_flow)
