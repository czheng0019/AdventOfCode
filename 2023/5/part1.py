# seedSoil = soilFert = fertWater = waterLight = lightTemp = tempHumid = humidLoc = {}
seeds = []
seedSoil = []
soilFert = []
fertWater = []
waterLight = []
lightTemp = []
tempHumid = []
humidLoc = []
remove = []
maps = {
    0: seeds,
    1: seedSoil,
    2: soilFert,
    3: fertWater,
    4: waterLight,
    5: lightTemp,
    6: tempHumid,
    7: humidLoc,
}
s = empty = False
count = -1
skip = 0

with open("input.txt", "r") as f:
    for line in f:
        if line.count("seeds") == 1:
            s = True
        if line == '\n':
            if count >= 0:
                if len(maps.get(count)) != 0:
                    for m in maps.get(count):
                        maps.get(count + 1).append(m)
                        remove.append(m)
                    for r in remove:
                        maps.get(count).remove(r)
                    remove.clear()
            count = count + 1
            skip = 0
            empty = False
        if skip >= 2:
            seedSoil = ()
            split = line.split(" ")
            second = split[0].strip()
            first = split[1].strip()
            size = split[2].strip()
            for o in maps.get(count):
                if int(first) <= int(o) < (int(first) + int(size)):
                    maps.get(count + 1).append(str(int(o) - int(first) + int(second)))
                    remove.append(o)
            for r in remove:
                maps.get(count).remove(r)
            remove.clear()
        if s:
            split = line.split(":")
            space = split[1].strip().split(" ")
            s = False
            for num in space:
                seeds.append(num.strip())
        skip = skip + 1

if len(maps.get(count)) != 0:
    for m in maps.get(count):
        maps.get(count + 1).append(m)
        remove.append(m)
    for r in remove:
        maps.get(count).remove(r)
    remove.clear()

humidLoc.sort(key=int)
print(humidLoc[0])
