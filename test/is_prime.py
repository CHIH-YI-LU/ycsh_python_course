a = int(input())
for i in range(2,a):
    if a % i ==0 :
        print("不是質數")
        break

else:
    print("是質數")    