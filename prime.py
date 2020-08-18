n = int(input('輸入大於 1 的整數: '))
if (n == 2):
    print('2 是質數')
else:
    for i in range(2, n):
        if (n % i ==0):
            print('%d 不是質數' % n) # %d 十進位輸出
            break
    else:
        print('該數是質數')