# x = (-b +- sqrt(b^2-4ac))/2a
# D = -x^2+Tx
# x = (-T +- sqrt(T^2-4*-1*D))/(2*-1)
import re
from math import sqrt, ceil, floor

count = 1
with open("input.txt", "r") as f:
    timeLine = f.readline()
    time = re.sub('[^0-9]', '', timeLine)

    distLine = f.readline()
    dist = re.sub('[^0-9]', '', distLine)
    print(time)
    print(dist)

t = int(time)
d = int(dist)

left = ceil((-t + sqrt((t ** 2) - (4 * d))) / -2)
right = floor((-t - sqrt((t ** 2) - (4 * d))) / -2)
if left * right == d:
    count *= right - left - 1
else:
    count *= right - left + 1

print(left, right)

print(count)
