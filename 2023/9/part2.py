arr = []
history = []
side = []
end = 0
odd = 1

with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for line in arr:
    split = line.split(" ")
    history = [int(i.strip()) for i in split]
    end += history[0]
    odd = -1
    while history.count(history[0]) != len(history):
        for i in range(len(history) - 1):
            side.append(int(history[i + 1]) - int(history[i]))
        history.clear()
        history = side.copy()
        side.clear()
        end += (history[0]) * odd
        odd *= -1

print(end)
