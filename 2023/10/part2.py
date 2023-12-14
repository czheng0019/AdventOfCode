prevY = 0
prevX = -1
x = 61
y = 10

count = 0
i = 1
start = "J"
arr = []
side = []
line = []
on = False
prev = 0

direct = {
    (0, 1, "-"): (0, -1),
    (0, -1, "-"): (0, 1),
    (1, 0, "|"): (-1, 0),
    (-1, 0, "|"): (1, 0),
    (0, -1, "7"): (1, 0),
    (1, 0, "7"): (0, -1),
    (-1, 0, "J"): (0, -1),
    (0, -1, "J"): (-1, 0),
    (0, 1, "L"): (-1, 0),
    (-1, 0, "L"): (0, 1),
    (1, 0, "F"): (0, 1),
    (0, 1, "F"): (1, 0),
}

with open("input.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]

arr.append((x, y))
x += direct.get((prevY, prevX, start))[1]
y += direct.get((prevY, prevX, start))[0]
prevX, prevY = -direct.get((prevY, prevX, start))[0], -direct.get((prevY, prevX, start))[1]

while grid[x][y] != "S":
    curr = grid[x][y]
    arr.append((x, y))
    x += direct.get((prevY, prevX, curr))[0]
    y += direct.get((prevY, prevX, curr))[1]
    prevX, prevY = -direct.get((prevY, prevX, curr))[1], -direct.get((prevY, prevX, curr))[0]

arr.sort(key=lambda a: a[0])

for x in arr:
    if x[0] > i:
        line.sort(key=lambda b: b[1])
        side.append(line)
        line = []
        i = i+1
    line.append((x[0], x[1]))

for tup in side:
    on = False
    for i in tup:
        if on and i[1] - prev > 1:
            count += i[1] - prev - 1
        if grid[i[0]][i[1]] in "|LJS":
            on = not on
        prev = i[1]

print(count)
