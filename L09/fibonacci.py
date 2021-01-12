F = [0,1]
m = int(input())

for n in range(2,m+1):
    Fn = F[n-1] + F[n-2]
    F.append(Fn)

print(F[m])    