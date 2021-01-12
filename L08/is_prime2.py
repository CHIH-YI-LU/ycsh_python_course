a = int(input())
i=2
while i < a:
    if a % i ==0:
        print("不是質數")
        break
    i = i + 1     
else:
    print("是質數")     
  