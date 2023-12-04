sum = red = green = blue = 0
with open("input.txt", "r") as f:
    for line in f:
        game = line.split(":")
        sets = game[1].strip().split(";")
        for s in sets:
            colors = s.split(", ")
            for i in colors:
                parts = i.strip().split(" ")
                if parts[1] == "red":
                    red = max(red, int(parts[0]))
                if parts[1] == "green":
                    green = max(green, int(parts[0]))
                if parts[1] == "blue":
                    blue = max(blue, int(parts[0]))
        sum += red * green * blue
        red = green = blue = 0

print(sum)



