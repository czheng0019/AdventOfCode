maps = []
mapp = []
one = []
two = []
remove = []
again = []
skip = 1
isOne = True
set = False

with open("input.txt", "r") as f:
    line = f.readline()
    split = line.split(":")
    space = split[1].strip().split(" ")
    for i in range(0, len(space), 2):
        pair = (int(space[i].strip()), int(space[i].strip()) + int(space[i+1].strip()))
        one.append(pair)
    print(one)
    f.readline()
    for line in f.readlines():
        if line == '\n':
            maps.append(mapp.copy())
            skip = 0
            mapp.clear()
        if skip >= 2:
            split = line.split(" ")
            nums = (int(split[0].strip()), int(split[1].strip()), int(split[2].strip()))
            mapp.append(nums)
        skip = skip + 1
    maps.append(mapp.copy())
    print(maps)

for section in maps:
    newest = []
    change = []
    for tup in section:
        if not set:
            if len(one) != 0:
                newest = one
                change = two
                isOne = True
            else:
                newest = two
                change = one
                isOne = False
            set = True
        for o in range(len(newest)):
            instr_range = (tup[1], tup[1] + tup[2])
            shift = tup[0] - tup[1]
            if instr_range[0] <= newest[o][0] and newest[o][1] <= instr_range[1]:
                change.append((newest[o][0] + shift, newest[o][1] + shift))
                remove.append(newest[o])
            elif newest[o][0] <= instr_range[0] and newest[o][1] >= instr_range[1]:
                again.append((newest[o][0], instr_range[0]))
                change.append((instr_range[0] + shift, instr_range[1] + shift))
                again.append((instr_range[1], newest[o][1]))
                remove.append(newest[o])
            elif instr_range[0] <= newest[o][0] < instr_range[1] <= newest[o][1]:
                change.append((newest[o][0] + shift, instr_range[1] + shift))
                again.append((instr_range[1], newest[o][1]))
                remove.append(newest[o])
            elif newest[o][0] < instr_range[0] < newest[o][1] <= instr_range[1]:
                again.append((newest[o][0], instr_range[0]))
                change.append((instr_range[0] + shift, newest[o][1] + shift))
                remove.append(newest[o])
        for r in remove:
            if isOne:
                one.remove(r)
            else:
                two.remove(r)
        remove.clear()
        for a in again:
            newest.append(a)
        again.clear()
    if isOne and len(one) != 0:
        for o in one:
            two.append(o)
        one.clear()
    elif not isOne and len(two) != 0:
        for t in two:
            one.append(t)
        two.clear()
    set = False
    print(one)
    print(two)


print(min(two, key=lambda x: x[0])[0])

