import math

r = float(input())
n = float(input())

a = math.sin(math.pi*2/n)
area = r ** 2 * a * n / 2

print(area)