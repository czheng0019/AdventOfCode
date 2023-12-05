arr = []
total = count = first = second = 0
up = down = False
num = ""
columns, rows = 140, 140
with open("input.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

for i in range(columns):
    for j in range(rows):
        if arr[i][j] == "*":
            up = down = False
            if j-1 >= 0 and arr[i][j-1].isnumeric():
                add = 1
                while j-add >= 0 and arr[i][j-add] != ".":
                    num += arr[i][j-add]
                    add = add+1
                num = num[::-1]
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if j+1 <= 139 and arr[i][j+1].isnumeric():
                add = 1
                while j+add <= 139 and arr[i][j+add] != ".":
                    num += arr[i][j+add]
                    add = add + 1
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if i-1 >= 0 and arr[i-1][j].isnumeric():
                add = 1
                num += arr[i-1][j]
                while j-add >= 0 and arr[i-1][j-add] != ".":
                    num += arr[i-1][j-add]
                    add = add+1
                add = 1
                num = num[::-1]
                while j+add <= 139 and arr[i-1][j+add] != ".":
                    num += arr[i-1][j+add]
                    add = add + 1
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
                up = True
            if i+1 <= 139 and arr[i+1][j].isnumeric():
                add = 1
                num += arr[i+1][j]
                while j-add >= 0 and arr[i+1][j-add] != ".":
                    num += arr[i+1][j-add]
                    add = add+1
                add = 1
                num = num[::-1]
                while j+add <= 139 and arr[i+1][j+add] != ".":
                    num += arr[i+1][j+add]
                    add = add + 1
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
                down = True
            if i-1 >= 0 and j - 1 >= 0 and arr[i-1][j - 1].isnumeric() and not up:
                add = 1
                while j-add >= 0 and arr[i-1][j-add] != ".":
                    num += arr[i-1][j-add]
                    add = add+1
                num = num[::-1]
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if i+1 <= 139 and j - 1 >= 0 and arr[i+1][j - 1].isnumeric() and not down:
                add = 1
                while j-add >= 0 and arr[i+1][j-add] != ".":
                    num += arr[i+1][j-add]
                    add = add+1
                num = num[::-1]
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if i+1 <= 139 and j+1 <= 139 and arr[i+1][j + 1].isnumeric() and not down:
                add = 1
                while j+add <= 139 and arr[i+1][j+add] != ".":
                    num += arr[i+1][j+add]
                    add = add+1
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if i-1 >= 0 and j+1 <= 139 and arr[i-1][j + 1].isnumeric() and not up:
                add = 1
                while j+add <= 139 and arr[i-1][j+add] != ".":
                    num += arr[i-1][j+add]
                    add = add+1
                print(num)
                if count == 0:
                    first = num
                elif count == 1:
                    second = num
                count = count+1
                num = ""
            if count == 2:
                total += int(first) * int(second)
            count = 0
            print(arr[i][j])
print(total)