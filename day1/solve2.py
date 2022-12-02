elves = []
new_elf = []
with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
             new_elf.append(int(line))
        elif new_elf:
            elves.append(new_elf)
            new_elf = []
if new_elf:
    elves.append(new_elf)
    new_elf = []

calories = list(sum(elf) for elf in elves)
calories.sort()
print(sum(calories[-3:]))
