h = float(input("請輸入身高（公分）:"))
w = float(input("請輸入體重（公斤）:"))

h = h/100
bmi = w/h**2
bmi = round(bmi,2)
print("BMI:",bmi)
