count = maximum = 0
with open("input.txt", "r") as f:
    for line in f:
        if line == '\n':
            maximum = max(count, maximum)
            count = 0
        else:
            count += int(line)
print(maximum)
