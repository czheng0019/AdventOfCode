count = i = 0
strg = last = first = ""
arr = []
nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for line in arr:
    for c in line:
        if c.isnumeric():
            if i == 0:
                first = c
            last = c
            i = i + 1
    for num in nums:
        if line.count(num) >= 1:
            if line.index(num) < line.index(first):
                first = num
            if line.rindex(num) > line.rindex(last):
                last = num
    if first in nums:
        first = nums.get(first)
    if last in nums:
        last = nums.get(last)
    strg += first
    strg += last
    count += int(strg)
    strg = ""
    i = 0

print(count)
