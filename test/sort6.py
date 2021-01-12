a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
i = 0
while i < 6:
    if f > e :
        f,e = e,f
    if e > d :
        e,d = d,e 
    if d > c :
        d,c = c,d    
    if c > b :
         c,b = b,c 
    if b > a :
         b,a = a,b 
    i = i +1     

print(a)   
print(b) 
print(c) 
print(d) 
print(e) 
print(f) 