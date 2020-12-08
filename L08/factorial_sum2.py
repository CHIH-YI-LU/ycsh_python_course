n = int(input())
a = 1
b = 1
i = 1
while i < n+1:
    a *= i
    b += a
    i = i +1
print(b)   