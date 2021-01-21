import random

a = random.randint(1,100)
i = 0
while i == 0 :
    b = int(input())
    if b > a :
        print("猜大了")
    elif b < a :
        print("猜小了")
    elif b == a :
        print("猜對了")
        break        