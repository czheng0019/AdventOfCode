total = count = 0
arr = []
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for line in arr:
    key = line.split("|")[0].split(":")[1].strip().split(" ")
    nums = line.split("|")[1].split()
    for num in nums:
        if num in key:
            count = count+1
    if count >= 1:
        total += 2**(count - 1)
    count = 0

print(total)
