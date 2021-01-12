F = [0,1]
x = int(input())
m = int(input())

for n in range(2,m+1):
    Fn = F[n-1] + F[n-2]
    F.append(Fn)
#print(F)
c = []
for z in range(x,m+1):
    #print(z)
   # print(F[z])
    c.append(F[z])
print(c)    