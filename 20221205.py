import re
import copy
import itertools


def performProcedure(stacksOfCrates, rearrangementProcedure):
    oldCrane = copy.deepcopy(stacksOfCrates)
    newCrane = copy.deepcopy(stacksOfCrates)

    for i in range(0, len(rearrangementProcedure)):
        procedure = rearrangementProcedure[i].split(" ")

        numOfItemsToMove = int(procedure[1])
        takeFromStack = int(procedure[3])
        placeIntoStack = int(procedure[5])

        for j in range(0, numOfItemsToMove):
            oldCrane[placeIntoStack].insert(0, oldCrane[takeFromStack].pop(0))

        craneRemovedItems = newCrane[takeFromStack][0:numOfItemsToMove]
        del newCrane[takeFromStack][0:numOfItemsToMove]

        newCrane[placeIntoStack] = craneRemovedItems + newCrane[placeIntoStack]

    return (oldCrane, newCrane)


def getTopCrates(stacksOfCrates):
    topCrates = ""

    for stacks in range(1, len(stacksOfCrates) + 1):
        topCrates = topCrates + stacksOfCrates[stacks][0].replace("[", "").replace("]", "")

    return topCrates


with open("5.in", "r", encoding="UTF-8") as str_file:
    str = str_file.read()

    drawing = str.split("\n\n")
    drawingOfCrates = drawing[0].split("\n")
    rearrangementProcedure = drawing[1].split("\n")

    horizontalCratesDrawing = [re.findall(r'.{1,4}', row) for row in drawingOfCrates[:-1]]

    initialStacksOfCrates = {}

    # create initial stacks from drawing
    for row in horizontalCratesDrawing:
        for index, crate in enumerate(row):
            crate = crate.strip()
            if crate != "":
                if index + 1 in initialStacksOfCrates:
                    initialStacksOfCrates[index + 1].append(crate)
                else:
                    initialStacksOfCrates[index + 1] = [crate]

    [oldCrane, newCrane] = performProcedure(initialStacksOfCrates, rearrangementProcedure)

    # part 1
    oldTopCrates = getTopCrates(oldCrane)
    print(oldTopCrates)

    # part 2
    newTopCrates = getTopCrates(newCrane)
    print(newTopCrates)



"""

use itertools::Itertools;

#[derive(Debug)]
struct Instruction {
    amount: usize,
    from: usize,
    to: usize,
}

fn parse_input() -> Option<(Vec<Vec<char>>, Vec<Instruction>)> {
    let input = std::fs::read_to_string("src/day05.txt").ok()?;
    let (left, instructions_str) = input.split_once("\n\n")?;
    let (stacks_str, platforms) = left.rsplit_once('\n')?;

    // parse crates
    let num_stacks = platforms.split_whitespace().last()?.parse().ok()?;
    let mut stacks = vec![Vec::new(); num_stacks];

    for line in stacks_str.lines().rev() {
        for (idx, mut chunk) in line.chars().chunks(4).into_iter().enumerate() {
            let second = chunk.nth(1)?;
            if second.is_alphabetic() {
                stacks[idx].push(second);
            }
        }
    }

    // parse instructions
    let mut instructions = Vec::new();
    for line in instructions_str.lines() {
        let rest = line.strip_prefix("move ")?;
        let (amount, rest) = rest.split_once(" from ")?;
        let (from, to) = rest.split_once(" to ")?;
        let instruction = Instruction {
            amount: amount.parse().ok()?,
            from: from.parse::<usize>().ok()? - 1,
            to: to.parse::<usize>().ok()? - 1,
        };
        instructions.push(instruction);
    }

    Some((stacks, instructions))
}

pub fn part_1() -> String {
    let (mut stacks, instructions) = parse_input().unwrap();
    for Instruction { amount, from, to } in instructions {
        for _ in 0..amount {
            if let Some(removed) = stacks[from].pop() {
                stacks[to].push(removed);
            }
        }
    }

    stacks
        .iter()
        .filter_map(|stack| stack.iter().last())
        .collect()
}

pub fn part_2() -> String {
    let (mut stacks, instructions) = parse_input().unwrap();
    for Instruction { amount, from, to } in instructions {
        let from_stack_len = stacks[from].len();
        let removed = stacks[from].split_off(from_stack_len - amount);
        stacks[to].extend(removed);
    }

    stacks
        .iter()
        .filter_map(|stack| stack.iter().last())
        .collect()
}
"""
"""

import sys

from copy import deepcopy
infile = sys.argv[1] if len(sys.argv)>1 else '5.in'
data = open(infile).read() #.strip()
lines = [x for x in data.split('\n')]

S = []
cmds = []
for line in lines:
    print(line, len(line))
    if line =='':
        break
    sz = (len(line)+1)//4
    while len(S) < sz:
        S.append([])
    for i in range(len(S)):
        ch = line[1 + 4*i]
        if ch != ' ' and 'A'<=ch<='Z':
            S[i].append(ch)
print(S)

S1 = deepcopy(S)
S2 = deepcopy(S)
found = False
for cmd in lines:
    if cmd == '':
        found = True
        continue
    if not found:
        continue
    words = cmd.split()
    qty = int(words[1])
    from_ = int(words[3]) - 1
    to_ = int(words[5]) - 1
    for (ST, do_rev) in [(S1, True), (S2, False)]:
        MOVE = ST[from_][:qty]
        ST[from_] = ST[from_][:qty]
        ST[to_] = (list(reversed(MOVE)) if do_rev else MOVE) + ST[to_]
print(''.join([s[0] for s in S1 if len(s)>0]))
print(''.join([s[0] for s in S2 if len(s)>0]))

"""