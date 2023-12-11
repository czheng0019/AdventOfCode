occDict = {}
arr = []
five, four, full, three, two, one, high = ([] for i in range(7))
chooseArr = []
allHands = []
i = 0
sum = 0
ranking = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line)


def sort(hand1, hand2, idx):
    a, b = hand1
    x, y = hand2
    if ranking.get(a[idx]) < ranking.get(x[idx]):
        return 1
    elif ranking.get(a[idx]) == ranking.get(x[idx]):
        return sort(hand1, hand2, idx + 1)
    else:
        return 0


for line in arr:
    split = line.split(" ")
    hand = split[0]
    bid = split[1].strip()
    for char in hand:
        alrdy = i = 0
        if occDict.get(char) is not None:
            alrdy = occDict.get(char)
        occDict.update({char: alrdy + 1})
    occ = list(occDict.values())
    if occ.count(5) == 1:
        chooseArr = five
    elif occ.count(4) == 1:
        chooseArr = four
    elif occ.count(3) == 1 and occ.count(2) == 1:
        chooseArr = full
    elif occ.count(3) == 1:
        chooseArr = three
    elif occ.count(2) == 2:
        chooseArr = two
    elif occ.count(2) == 1:
        chooseArr = one
    else:
        chooseArr = high

    if len(chooseArr) == 0:
        chooseArr.append((hand, bid))
    else:
        while i <= len(chooseArr) - 1 and sort(chooseArr[i], (hand, bid), 0) == 1:
            i = i + 1
        chooseArr.insert(i, (hand, bid))

    occDict.clear()

allHands.append(five)
allHands.append(four)
allHands.append(full)
allHands.append(three)
allHands.append(two)
allHands.append(one)
allHands.append(high)

i = len(arr)

for group in allHands:
    for g in group:
        sum += i * int(g[1])
        i = i-1

print(sum)


