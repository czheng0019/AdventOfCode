count = 0
arr = []
with open("input.txt", "r") as f:
    for line in f:
        if line == '\n':
            arr.append(count)
            count = 0
        else:
            count += int(line)
arr.sort(reverse=True)
print(sum(arr[:3]))
