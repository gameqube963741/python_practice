def isTaiwanPhone(str):
    if len(str) != 11:
        return False
    
    for i in range(0, 11):
        if i ==4:
            if str[4] != '-':
                return False
        else:
            if str[i].isdecimal() == False: #檢查十進制
                return False
    return True

print('0977-177998', isTaiwanPhone('0977-177998'))

# 如過格式產生改變程式就會失效 所以選擇使用正規表達式