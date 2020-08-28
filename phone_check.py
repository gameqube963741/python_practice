def isTaiwanPhone(str):
    if len(str) != 11:
        return False
    #檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i ==4:
            if str[4] != '-':               #如果第5個字元不是'-'字元 
                return False                #傳回非手機號碼格式
        else:
            if str[i].isdecimal() == False: #檢查十進制
                return False                #傳回非手機號碼格式
    return True                             #傳回是正確手機號碼格式

print('0977-177998', isTaiwanPhone('0977-177998'))

# 如過格式產生改變程式就會失效 所以選擇使用正規表達式