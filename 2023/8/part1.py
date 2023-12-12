arr = []
nodes = {}
curr = "AAA"
i = 0
c = 0

with open("input.txt", "r") as f:
    inst = f.readline().strip()
    f.readline()
    for line in f:
        arr.append(line.strip())

for line in arr:
    split = line.split("=")
    node = split[0].strip()
    split2 = split[1].split(", ")
    lr = (split2[0].split("(")[1].strip(), split2[1].split(")")[0].strip())
    nodes.update({node: lr})

while curr != "ZZZ":
    if inst[i % len(inst)] == 'L':
        c = 0
    else:
        c = 1
    curr = nodes.get(curr)[c]
    i = i + 1

print(i)
