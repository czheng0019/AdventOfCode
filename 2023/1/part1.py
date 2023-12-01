count = i = 0
str = last = ""
arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for line in arr:
    for c in line:
        if c.isnumeric():
            if i == 0:
                str += c
            last = c
            i = i+1
    str += last
    count += int(str)
    str = ""
    i = 0

print(count)
