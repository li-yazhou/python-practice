temp = input('输入你的成绩')
score = int(temp)
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
elif score >=0 and score < 60:
    print('E')
else:
    print('输入有误，请重新输入')
