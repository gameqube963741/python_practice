# sum = 0 
# n = int(input('輸入整數:'))
# for i in range(1, n+1):
#     sum+=i
# print('1 到 %d 的整數和 為 %d '%(n,sum))

# sum = 0
# n = int(input('輸入正整數:'))
# for i in range(1, n+1):
#     sum += i
# print('1 到 %d 的整數和 為 %d'%(n,sum))

# n=0
# for i in range(1,101):
#     for j in range(1,101):
#         n += 1
# print(n)


# for i in range(1,10):
#     for j in range(1,10):
#         product = i * j
#         print('%d * %d = %-2d' %(i, j, product),end=' ')
#     print()

# for i in range(1,11):
#     if(i == 6):
#         break
#     print(i, end = ', ')
    
import os
dir = 'mydir'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
   print(dir + '資料夾已存在')

import os 
dir = 'mydir'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + '資料夾已存在')