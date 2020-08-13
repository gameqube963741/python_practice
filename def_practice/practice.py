# def GetArea(width, height):
#     area = width * height
#     return area

# ret1 = GetArea(6,9) #ret1 = 54
# print(ret1)

# def Circle(radius)

# def ctof(c):
#     f = c * 1.8 + 32
#     return f

# inputc = float(input("輸入攝氏溫度:"))
# print("華氏溫度為：%5.1f 度" % ctof(inputc))

# list = ['This','is','a','book','This','This']
# # print(' '.join(list))
# c_this = list.count('This')
# print(c_this)

import sys
result=[]
with open(r'/Users/edward/Desktop/python_practice/def_practice/data.txt', 'r' , encoding= 'utf-8-sig') as f:
    for line in f:
        result.append(list(line.strip('\n').split(',')))
print(result)
