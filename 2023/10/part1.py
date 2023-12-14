prevY = -1
prevX = 0
x = 61
y = 10
count = 1

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

x += direct.get((prevY, prevX, "J"))[1]
y += direct.get((prevY, prevX, "J"))[0]
prevX, prevY = -direct.get((prevY, prevX, "J"))[0], -direct.get((prevY, prevX, "J"))[1]

while grid[x][y] != "S":
    curr = grid[x][y]
    x += direct.get((prevY, prevX, curr))[0]
    y += direct.get((prevY, prevX, curr))[1]
    prevX, prevY = -direct.get((prevY, prevX, curr))[1], -direct.get((prevY, prevX, curr))[0]
    count = count+1

print(count//2)
