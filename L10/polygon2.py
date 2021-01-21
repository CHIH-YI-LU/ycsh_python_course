import math
def a(r,n):
    return r ** 2 * math.sin(math.pi*2/n) / 2 * n
r = float(input())
n = float(input())

area = a(r,n)

print(area)


