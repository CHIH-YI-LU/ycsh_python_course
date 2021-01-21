import random

def b(c):
    if c > a :
        print("猜大了")
    elif c < a :
        print("猜小了")
    elif c == a :
        print("猜對了")    
    return a    
a = random.randint(1,100)
i = 0
while i == 0 :
    c = int(input())
    d = b(c)

print(d)