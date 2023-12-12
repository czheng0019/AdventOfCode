from functools import reduce

arr = []
nodes = {}
curr = []
side = []
amt = []
complete = num = i = c = nextI = 0
product = 1

with open("input.txt", "r") as f:
    inst = f.readline().strip()
    f.readline()
    for line in f:
        arr.append(line.strip())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for line in arr:
    split = line.split("=")
    node = split[0].strip()
    split2 = split[1].split(", ")
    if node[2] == 'A':
        num = num + 1
        curr.append(node)
    lr = (split2[0].split("(")[1].strip(), split2[1].split(")")[0].strip())
    nodes.update({node: lr})

while complete != num:
    for n in curr:
        if inst[i % len(inst)] == 'L':
            c = 0
        else:
            c = 1
        if nodes.get(n)[c][2] != 'Z':
            side.append(nodes.get(n)[c])
        else:
            complete = complete + 1
            amt.append(i + 1)
    i = i + 1
    curr.clear()
    curr = side.copy()
    side.clear()

for i in range(len(amt)):
    if i == 0:
        nextI = amt[i]
    else:
        nextI = gcd(nextI, amt[i])


def lcm(x, y):
    return (x * y) // gcd(x, y)


product = reduce(lambda x, y: x * y, amt)
nextI = reduce(lcm, amt)

print(nextI)
