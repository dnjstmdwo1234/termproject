import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import font_manager, rc
from matplotlib import style

with open('new_user_age_data_processing.csv', 'r') as raw:
    lines = raw.readlines()
cooked = csv.reader(lines)
user_age = []
user_num = []


for record in cooked:
    user_age.append(record[0])
    user_num.append(record[1])

# 데이터 내에서 몇 열까지 10대인지 index에 저장해서 총 10대 이용자의 합을 구하는 코드. 
index = 0
user_num_complete = []

user_num_10 = 0
while user_age[index] == '~10':
    user_num_10 = int(user_num[index]) + user_num_10
    index = index+1
user_num_complete.append(user_num_10)


user_num_70 = 0
while user_age[index] == '70~':
    user_num_70 = int(user_num[index]) + user_num_70
    index = index+1
user_num_complete.append(user_num_70)


user_num_60 = 0
while user_age[index] == '60':
    user_num_60 = int(user_num[index]) + user_num_60
    index = index+1
user_num_complete.append(user_num_60)


user_num_50 = 0
while user_age[index] == '50':
    user_num_50 = int(user_num[index]) + user_num_50
    index = index+1
user_num_complete.append(user_num_50)


user_num_40 = 0
while user_age[index] == '40':
    user_num_40 = int(user_num[index]) + user_num_40
    index = index+1
user_num_complete.append(user_num_40)


user_num_30 = 0
while user_age[index] == '30':
    user_num_30 = int(user_num[index]) + user_num_30
    index = index+1
user_num_complete.append(user_num_30)

user_num_20 = 0
while user_age[index] == '20':
    user_num_20 = int(user_num[index]) + user_num_20
    index = index+1
    if index == 8095:
        break
    else:
        continue
user_num_complete.append(user_num_20)

print(user_num_complete)

# 10대 이하 이용자수 : 26211 | 20대 이용자수 : 315035 | 30대 이용자수 : 138145 | 40대 이용자수 71412 | 
# 50대 이용자수 : 28412 | 60대 이용자수 : 6178 | 70대 이상 이용자수 : 77705 |
# print(user_num_complete)

# 주어진 데이터를 시각화 하여 표현하기 위하여 pie 그래프로 각 연령대 별로 나타내는 코드이다.
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

age = ['10대 이하','70대 이상','60대','50대','40대','30대','20대']

plt.pie(user_num_complete, labels=age, shadow=True, startangle=90)
plt.show()


