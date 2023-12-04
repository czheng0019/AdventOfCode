sum = 0
maxRed = 12
maxGreen = 13
maxBlue = 14
out = False
with open("input.txt", "r") as f:
    for line in f:
        game = line.split(":")
        sets = game[1].strip().split(";")
        for s in sets:
            colors = s.split(", ")
            for i in colors:
                parts = i.strip().split(" ")
                if parts[1] == "red":
                    if int(parts[0]) > maxRed:
                        out = True
                if parts[1] == "green":
                    if int(parts[0]) > maxGreen:
                        out = True
                if parts[1] == "blue":
                    if int(parts[0]) > maxBlue:
                        out = True
        if not out:
            sum += int(game[0].split(" ")[1])
        out = False

print(sum)



