# x = (-b +- sqrt(b^2-4ac))/2a
# D = -x^2+Tx
# x = (-T +- sqrt(T^2-4*-1*D))/(2*-1)
from math import sqrt, ceil, floor

count = 1
with open("input.txt", "r") as f:
    timeLine = f.readline()
    time = [int(t.strip()) for t in timeLine[5:].split(" ") if t != '']

    distLine = f.readline()
    dist = [int(d.strip()) for d in distLine[9:].split(" ") if d != '']
    print(time)
    print(dist)

for t, d in zip(time, dist):
    left = ceil((-t + sqrt((t**2) - (4 * d))) / -2)
    right = floor((-t - sqrt((t**2) - (4 * d))) / -2)
    if left * right == d:
        count *= right - left - 1
    else:
        count *= right - left + 1

    print(left, right)

print(count)
