import random
height = random.randint(150,200) / 100
weight = random.randint(60,100)
bmi = weight / (height * height)
print("你的BMI是", bmi)
if bmi < 18.5:
    print("體重過輕")
elif bmi >= 18.5 and bmi < 24:
    print("體重正常")   
elif bmi >= 24 and bmi < 27:
    print("體重過重")
elif bmi >= 27 and bmi < 30:
    print("輕度肥胖")
elif bmi >= 30 and bmi < 35:
    print("中度肥胖")
else:
    print("重度肥胖")