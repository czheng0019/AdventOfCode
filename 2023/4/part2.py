total = count = index = 0
arr = values = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

values = [1] * len(arr)

for line in arr:
    key = line.split("|")[0].split(":")[1].strip().split(" ")
    nums = line.split("|")[1].split()
    for num in nums:
        if num in key:
            count = count + 1
    if count >= 1:
        for i in range(1, count+1):
            values[index + i] = values[index + i] + values[index]
        print(values)
    count = 0
    index = index + 1

for value in values:
    total += value
print(total)
