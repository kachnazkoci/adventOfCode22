s = [i.strip() for i in open('1.in')]

calories = []
for elf in ('\n'. join(s)).split('\n\n'):
    cal = 0
    for j in elf.split('\n'):
        cal += int(j)
    calories.append(cal)
calories = sorted(calories)
print(calories[-1])
print(calories[-1]+calories[-2]+calories[-3])