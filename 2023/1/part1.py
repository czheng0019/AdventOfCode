count = i = 0
strg = last = ""
arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for line in arr:
    for c in line:
        if c.isnumeric():
            if i == 0:
                strg += c
            last = c
            i = i+1
    strg += last
    count += int(strg)
    strg = ""
    i = 0

print(count)
